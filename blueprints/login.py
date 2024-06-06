from flask import Blueprint, render_template, request, redirect, session, flash
from werkzeug.security import check_password_hash
from model.models import db, User

login = Blueprint(
    "login", __name__, static_folder="static", template_folder="view"
)

logout = Blueprint(
    "logout", __name__, static_folder="static", template_folder="view"
)

users = []

@login.route("/login", methods=["GET", "POST"])
def login_blueprint():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        session["user"] = user.username
        session["role"] = user.role
        return redirect("/home")

    return render_template("login.html", error="Error: Invalid credentials.")

@logout.route("/logout")
def logout_blueprint():
    session.clear()
    return redirect("/")