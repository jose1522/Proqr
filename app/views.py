from app import app
from flask import render_template, url_for, session, jsonify, make_response, g, redirect, abort, flash
from flask import request as req
from app.objects.Integration.DB.login import UserLogin
from app.objects.Integration.DB.userData import FetchUserData

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


@app.route("/user/new")
def new_user():
    return render_template("public/user_form.html",
                           isIndex=True,
                           showID = 'none',
                           showPassword='flex', # Shows the password field
                           userId="",
                           firstName="",
                           lastName="",
                           email="",
                           password="")


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
                           password=user.password)


@app.route("/user/modify")
def edit_user():
    return render_template("public/user_form.html",
                           isIndex=False,
                           showID='flex',
                           showPassword='none',
                           userId="",
                           firstName="",
                           lastName="",
                           email="",
                           password="")


@app.route("/user/delete")
def delete_user():
    return render_template("public/user_form.html",
                           isIndex=False,
                           showID='flex',
                           showPassword='none',
                           userId="",
                           firstName="",
                           lastName="",
                           email="",
                           password="")