from flask import Blueprint, render_template, session, redirect

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home.route("/")
@home.route("/home")
def home_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("home.html")
