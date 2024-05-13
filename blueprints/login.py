from flask import Blueprint, render_template, request, redirect, session
from blueprints.user import users

login = Blueprint(
    "login", __name__, static_folder="static", template_folder="templates"
)

@login.route("/login", methods=["GET", "POST"])
def login_blueprint():
    if request.method == "GET":
        return render_template("login.html")

    user = request.form["user"]
    password = request.form["password"]

    if user in users and users[user] == password:
        session.clear()
        session["user"] = user
        session["username"] = user[0 : user.index("@")]
        return redirect("/home")

    return render_template("login.html", error="Error: Invalid credentials.")
