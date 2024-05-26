from flask import Blueprint, render_template, request, redirect, session, flash
from blueprints.user import users

login = Blueprint(
    "login", __name__, static_folder="static", template_folder="templates"
)

logout = Blueprint(
    "logout", __name__, static_folder="static", template_folder="templates"
)

@login.route("/login", methods=["GET", "POST"])
def login_blueprint():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form["user"]
    password = request.form["password"]

    for user in users:
        if user["email"] == email and user["password"] == password:
            session.clear()
            session["user"] = email
            session["username"] = email[0 : email.index("@")]
            return redirect("/home")

    return render_template("login.html", error="Error: Invalid credentials.")

@logout.route("/logout")
def logout_blueprint():
    session.clear()
    return redirect("/")