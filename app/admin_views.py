from app import app  # Imports object from __init__.py
from flask import render_template


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

