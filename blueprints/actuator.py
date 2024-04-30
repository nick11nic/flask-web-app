from flask import Blueprint, render_template

actuator = Blueprint(
    "actuator", __name__, static_folder="static", template_folder="templates"
)


@actuator.route("/actuator")
def actuator_blueprint():
    return render_template("actuator.html")
