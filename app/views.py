from app import app
from flask import render_template, url_for, session, jsonify, make_response, g, redirect, abort, flash
from functools import wraps
import datetime

from flask import request as req
from app.objects.Integration.DB.login import UserLogin
from app.objects.Integration.DB.userData import FetchUserData
from app.objects.Integration.DB.modifyUser import ModifyUser
from app.objects.Integration.DB.deleteUser import DeleteUser
from app.objects.Integration.DB.addUser import AddUser
from app.objects.Integration.DB.recoverPassword import RecoverPassword
from app.objects.user import User
from app.objects.role import roleNumberToString
from app.objects.role import roleStringToNumber
from app.objects.role import getRoles
from app.objects.requestStatus import status
from app.objects.requestStatus import statusNumberToString
from app.objects.requestStatus import statusStringToNumber
from app.objects.requestStatus import getStatus
from app.objects.Integration.DB.userList import UserList
from app.objects.purchaseRequest import PurchaseRequest
from app.objects.Integration.DB.addRequest import AddRequest
from app.objects.Integration.DB.modifyRequest import ModifyRequest
from app.objects.Integration.DB.deleteRequest import DeleteRequest
from app.objects.Integration.DB.myRequestList import MyRequestList
from app.objects.Integration.DB.RequestList import RequestList
from app.objects.Integration.DB.requestData import FetchPurchaseData
from app.objects.Integration.DB.isAdmin import IsAdmin
from app.objects.Integration.DB.stats import Stats


# Este metodo fuerza al usuario a iniciar sesión
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))

    return wrap


# Endpoint para visualizar la pagina del login.
@app.route("/", methods=['GET', 'POST'])
def index():
    if req.method == 'GET':
        if 'user' in session:
            return redirect(url_for('home'))
        else:
            return render_template("public/index.html")
    else:  # Instrucciones para metodo post
        email = req.form['inputEmail']
        password = req.form['inputPassword']
        login = UserLogin(password, email)
        response = login.Authenticate()
        if response['Result'] == 'TRUE':
            session['user'] = response['Id']
            session['role'] = response['Role']
            session['email'] = email
            session['name'] = response['Name']
            return redirect(url_for('home'))
        else:
            return redirect(url_for('index'))


# Endpoint para recuperar contrasenna
@app.route("/recover_password", methods=['POST'])
def recover_password():
    form = req.form
    r = req
    if 'userUserID' in form:  # Seccion para cuando se recibe desde editar usuario
        id = form['userUserID']
        email = form['userUserEmail']
        u = User(userid=id, email=email)
        RecoverPassword(u)
    elif 'recoveryEmail' in form:  # Seccion para cuando se recibe desde recuperar contrasenna
        email = form['recoveryEmail']
        u = User(email=email)
        RecoverPassword(u)
    else:
        pass
    url = req.referrer
    return redirect(url)


# Endpoint para finalizar sesion
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return render_template("public/index.html")


# Endpoint para el landing page
@app.route("/home")
@login_required
def home():
    return render_template("public/home.html",
                           role=session['role'],
                           isAdmin=IsAdmin(session['user']),
                           name=session['name'])


# Endpoint para generar un nuevo purchase request
@app.route("/purchase/new", methods=['GET', 'POST'])
@login_required
def newPurchaseRequest():
    if req.method == 'POST':
        form = req.form
        userid = form['purchaseUserID']
        description = form['purchaseDescription']
        items = form['purchaseItems']
        comments = form['purchaseComments']
        amount = form['purchaseAmount']

        purchaserequest = PurchaseRequest(userid=userid, description=description, items=items, comments=comments,
                                          amount=amount, status="1")
        AddRequest(purchaserequest, session['email'])

        return redirect(url_for('purchase_list'))

    else:  # Seccion que muestra un formulario vacio
        return render_template("public/purchase_form.html",
                               isIndex=True,
                               role=session['role'],
                               showID="none",
                               showStatus="none",
                               userid=session['user'],
                               description='',
                               items='',
                               comments='',
                               amount='',
                               status='')


# Dynamic URL that shows a form for any purchase id
@app.route("/purchase/<id>")
@login_required
def purchase_info(id):
    purchase = FetchPurchaseData(id)
    return render_template("public/purchase_form.html",
                           isIndex=False,
                           showID='flex',
                           role=session['role'],
                           descriptionReadOnly='True',
                           itemsReadOnly='True',
                           amountReadOnly='True',
                           requestID=purchase.requestid,
                           userid=purchase.userid,
                           description=purchase.description,
                           items=purchase.items,
                           comments=purchase.comments,
                           amount=purchase.amount,
                           status=statusNumberToString(purchase.status),
                           statusList=getStatus(),
                           isOpen=purchase.isOpen(int(session['role'])),
                           statusid=purchase.status,
                           )


# Endpoint todos los requests con respecto al usuario de la sesion
@app.route("/purchase/all")
@login_required
def purchase_list():
    user = session['user']
    plist = MyRequestList(user)
    plist.FetchPurchaseList()

    return render_template("public/purchase_table.html", purchases=plist.purchases, sessionrole=int(session['role']))


# Endpoint todos los requests por un status específico y un usuario
@app.route("/purchase/all/<status>")
@login_required
def filtered_purchase_list(status):
    status = str.lower(status)
    if status in ("open", "closed"):
        user = session['user']
        role = session['role']
        plist = RequestList(userRole=role, userID=user, action=status)
        plist.FetchPurchaseList()

        return render_template("public/purchase_table.html", purchases=plist.purchases,
                               sessionrole=int(session['role']))
    else:
        return redirect(url_for('index'))


# Endpoint para modificar un purchase request
@app.route("/purchase_request/modify", methods=['GET', 'POST'])
@login_required
def modifyPurchaseRequest():
    if req.method == 'POST':
        form = req.form
        requestid = form['formID']
        userid = form['purchaseUserID']
        description = form['purchaseDescription']
        items = form['purchaseItems']
        comments = form['purchaseComments']
        amount = form['purchaseAmount']

        if 'approvedBtn' in form:
            status = session['role']
        elif 'rejectedBtn' in form:
            status = "4"
        else:
            status = "1"

        if requestid:
            modifyPurchaseRequest = PurchaseRequest(requestid=requestid,
                                                    userid=userid,
                                                    description=description,
                                                    items=items,
                                                    comments=comments,
                                                    amount=amount,
                                                    status=status)
            ModifyRequest(modifyPurchaseRequest, session['email'])

            if status in ("2", "3", "4"):
                return redirect("/purchase/all/open")
            else:
                return redirect("/purchase/{0}".format(requestid))
        else:
            return redirect(url_for('home'))

    else:  # Seccion que muestra un formulario vacio
        return render_template("public/purchase_request_form.html",
                               isIndex=True,
                               requestid='',
                               description='',
                               items='',
                               comments='',
                               amount='',
                               status=statusNumberToString(1),
                               statusList=getStatus())


# Endpoint para eliminar un purchase request
@app.route("/purchase_request/delete", methods=['GET', 'POST'])
@login_required
def deletePurchaseRequest():
    if req.method == 'POST':
        form = req.form
        requestid = form['formID']

        if requestid:
            deletePurchaseRequest = PurchaseRequest(requestid=requestid, status=0)
            DeleteRequest(deletePurchaseRequest)
            return redirect(url_for('purchase_list'))
        else:
            return redirect(url_for('home'))

    else:  # Seccion que muestra un formulario vacio
        return render_template("public/purchase_request_form.html",
                               isIndex=True,
                               requestid='',
                               description='',
                               items='',
                               comments='',
                               amount='',
                               status='')


# Endpoint para visualizar purchase orders
@app.route("/purchase_order")
@login_required
def purchaseOrder():
    return render_template("public/purchase_form.html")


# Endpoint para visualizar requests
@app.route("/requests")
@login_required
def request():
    return render_template("public/home.html")


# Endpoint para ver el profile
@app.route("/profile")
@login_required
def profile():
    return render_template("public/home.html")


# Endpoint para acceder a pagina de admin
@app.route("/admin")
@login_required
def admin():
    return render_template("public/home.html")


# Endpoint para acceder a reportes
@app.route("/reporting")
@login_required
def reporting():
    return render_template("admin/dashboard.html",
                           role = session['role'])


@app.route("/data-test")
@login_required
def dashboardData():

    data = Stats(session['role'], session['user'])
    data = data.GetData()
    return data


# Dynamic URL that shows a form for any user id
@app.route("/user/<id>")
@login_required
def user_info(id):
    user = FetchUserData(id)
    return render_template("public/user_form.html",
                           isIndex=False,
                           showID='flex',
                           showPassword='none',  # Hides password
                           userId=user.userId,
                           firstName=user.firstName,
                           lastName=user.lastName,
                           email=user.email,
                           password=user.password,
                           role=roleNumberToString(user.role),
                           roleList=getRoles())


# Endpoint para visualizar todos los usuarios
@app.route("/user/all")
@login_required
def user_list():
    uList = UserList()
    uList.FetchUserList()

    return render_template("public/user_table.html", users=uList.users)


# Endpoint para modificar un usuario
@app.route("/user/modify", methods=['GET', 'POST'])
@login_required
def edit_user():
    if req.method == 'POST':
        form = req.form
        id = form['userUserID']
        name = form['userUserFirstName']
        lastName = form['userUserLastName']
        email = form['userUserEmail']
        role = form['inputRole']

        if id:
            user = User(userid=id, firstname=name, lastname=lastName, email=email,
                        role=roleStringToNumber(role))  # to do: modify role
            print(user.role)
            ModifyUser(user)
            return redirect("/user/{0}".format(id))
        else:
            return redirect(url_for('home'))
    else:  # Seccion que muestra un formulario vacio
        return render_template("public/user_form.html",
                               isIndex=False,
                               showID='flex',
                               showPassword='none',
                               userId="",
                               firstName="",
                               lastName="",
                               email="",
                               password="")


# Endpoint para eliminar un usuario
@app.route("/user/delete", methods=['GET', 'POST'])
@login_required
def delete_user():
    if req.method == 'POST':
        form = req.form
        id = form['userUserID']

        if id:
            user = User(userid=id, status=0)
            DeleteUser(user)
            return redirect("/user/all".format(id))
        else:
            return redirect(url_for('home'))

    else:
        return render_template("public/user_form.html",
                               isIndex=False,
                               showID='flex',
                               showPassword='none',
                               userId="",
                               firstName="",
                               lastName="",
                               email="",
                               password="")


# Endpoint para agregar un usuario
@app.route("/user/add", methods=['GET', 'POST'])
@login_required
def add_user():
    if req.method == 'POST':
        form = req.form
        name = form['userUserFirstName']
        lastName = form['userUserLastName']
        email = form['userUserEmail']
        role = form['inputRole']

        # password = form['userUserPassword'] # Generating password automatically
        user = User(firstname=name, lastname=lastName, email=email, role=roleStringToNumber(role))  # to do: modify role
        print(user.role)
        AddUser(user)

        return redirect("/user/all")

    else:
        return render_template("public/user_form.html",
                               isIndex=True,
                               showID='none',
                               showPassword='none',
                               userId="",
                               firstName="",
                               lastName="",
                               email="",
                               password="",
                               roleList=getRoles())

