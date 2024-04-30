from flask import Blueprint, render_template, redirect, session

sensor = Blueprint(
    "sensor", __name__, static_folder="static", template_folder="templates"
)


@sensor.route("/sensor")
def sensor_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("sensor.html")
