from app import app
from flask import render_template, request, url_for, session, jsonify, make_response, g, redirect, abort, flash

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/home")
def home():
    return render_template("public/home.html")


@app.route("/purchase_order/new")
def newPurchaseOrder():
    return render_template("public/purchase_form.html")


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