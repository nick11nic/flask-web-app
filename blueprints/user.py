from flask import Blueprint, render_template, session, redirect

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")


@user.route("/user")
def user_blueprint():
    if session["username"] == "admin":
        return render_template("user.html")

    return redirect("/home")
