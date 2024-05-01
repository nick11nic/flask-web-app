from flask import Blueprint, session, redirect

logout = Blueprint(
    "logout", __name__, static_folder="static", template_folder="templates"
)


@logout.route("/logout")
def logout_blueprint():
    session.clear()
    return redirect("/")
