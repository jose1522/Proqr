from app import app
from flask import render_template, url_for, session, jsonify, make_response, g, redirect, abort, flash
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
from app.objects.Integration.DB.userList import UserList

@app.route("/", methods=['GET', 'POST'])
def index():
    if req.method == 'GET':
        return render_template("public/index.html")
    else:
        email = req.form['inputEmail']
        password = req.form['inputPassword']
        login = UserLogin(password,email)
        response = login.Authenticate()
        if response['Result'] == 'TRUE':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('index'))


@app.route("/recover_password", methods=['POST'])
def recover_password():
    form = req.form
    r = req
    if 'userUserID' in form:
        id = form['userUserID']
        u = User(userid=id)
        RecoverPassword(u)
    elif 'recoveryEmail' in form:
        email = form['recoveryEmail']
        u = User(email=email)
        RecoverPassword(u)
    else:
        pass
    url = req.referrer
    return redirect(url)


@app.route("/logout")
def logout():
    return render_template("public/index.html")


@app.route("/home")
def home():
    return render_template("public/home.html")


@app.route("/purchase_order/new")
def newPurchaseOrder():
    return render_template("public/purchase_form.html", isIndex=True)


@app.route("/purchase_order/modify")
def modifyPurchaseOrder():
    return render_template("public/purchase_form.html", isIndex=False)


@app.route("/purchase_order")
def purchaseOrder():
    return render_template("public/purchase_form.html")


@app.route("/requests")
def request():
    return render_template("public/home.html")


@app.route("/profile")
def profile():
    return render_template("public/home.html")


@app.route("/admin")
def admin():
    return render_template("public/home.html")


@app.route("/reporting")
def reporting():
    return render_template("public/home.html")


# @app.route("/user/new")
# def new_user():
#     return render_template("public/user_form.html",
#                            isIndex=True,
#                            showID = 'none',
#                            showPassword='flex', # Shows the password field
#                            userId="",
#                            firstName="",
#                            lastName="",
#                            email="",
#                            password="")


@app.route("/user/<id>") # Dynamic URL that shows a form for any user id
def user_info(id):
    user = FetchUserData(id)
    return render_template("public/user_form.html",
                           isIndex=False,
                           showID='flex',
                           showPassword='none', # Hides password
                           userId=user.userId,
                           firstName=user.firstName,
                           lastName=user.lastName,
                           email=user.email,
                           password=user.password,
                           role=roleNumberToString(user.role),
                           roleList=getRoles())


@app.route("/user/all")
def user_list():
    uList = UserList()
    uList.FetchUserList()

    return render_template("public/user_table.html", users=uList.users)


@app.route("/user/modify", methods=['GET','POST'])
def edit_user():
    if req.method == 'POST':
        form = req.form
        id = form['userUserID']
        name = form['userUserFirstName']
        lastName = form['userUserLastName']
        email = form['userUserEmail']
        role = form['inputRole']

        if id:
            user = User(userid=id, firstname=name, lastname=lastName, email=email, role=roleStringToNumber(role)) # to do: modify role
            print(user.role)
            ModifyUser(user)
            return redirect("/user/{0}".format(id))
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


@app.route("/user/delete", methods=['GET','POST'])
def delete_user():
    if req.method == 'POST':
        form = req.form
        id = form['userUserID']

        if id:
            user = User(userid=id)
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

@app.route("/user/add", methods=['GET','POST'])
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