from app import app
from flask import render_template, request, url_for, session, jsonify, make_response, g, redirect, abort, flash

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/home")
def about():
    return render_template("public/home.html")

