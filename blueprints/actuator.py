from flask import Blueprint, render_template, session, redirect

actuator = Blueprint(
    "actuator", __name__, static_folder="static", template_folder="templates"
)


@actuator.route("/actuator")
def actuator_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("actuator.html")
