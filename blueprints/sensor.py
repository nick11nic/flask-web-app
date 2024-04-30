from flask import Blueprint, render_template

sensor = Blueprint(
    "sensor", __name__, static_folder="static", template_folder="templates"
)


@sensor.route("/sensor")
def sensor_blueprint():
    return render_template("sensor.html")
