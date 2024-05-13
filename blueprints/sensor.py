from flask import Blueprint, render_template, redirect, request, session

sensor = Blueprint("sensor", __name__, static_folder="static", template_folder="templates")

sensors = [{"id": 1, "name": "Sensor 1", "value": "0"},]

@sensor.route("/sensor")
def sensor_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("sensor.html", sensors=sensors)

@sensor.route("/create_sensor", methods=["POST"])
def create_sensor():
    global sensors
    name = request.form.get("name")
    value = request.form.get("value")
    sensor_id = len(sensors) + 1
    new_sensor = {"id": sensor_id, "name": name, "value": value}
    sensors.append(new_sensor)
    return redirect("/sensor")

@sensor.route("/delete_sensor/<int:sensor_id>", methods=["POST"])
def delete_sensor(sensor_id):
    global sensors
    for sensor in sensors:
        if sensor["id"] == sensor_id:
            sensors.remove(sensor)
            break
    return redirect("/sensor")


