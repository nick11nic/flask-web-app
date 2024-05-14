from flask import Blueprint, render_template, redirect, request, session

actuator = Blueprint("actuator", __name__, static_folder="static", template_folder="templates")

actuators = [{"id": 1, "name": "Actuator 1", "value": "0"},]

@actuator.route("/actuator")
def actuator_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("actuator.html", actuators=actuators)

@actuator.route("/create_actuator", methods=["POST"])
def create_actuator():
    global actuators
    name = request.form.get("name")
    value = request.form.get("value")
    actuator_id = len(actuators) + 1
    new_actuator = {"id": actuator_id, "name": name, "value": value}
    actuators.append(new_actuator)
    return redirect("/actuator")

@actuator.route("/delete_actuator/<int:actuator_id>", methods=["POST"])
def delete_actuator(actuator_id):
    global actuators
    for actuator in actuators:
        if actuator["id"] == actuator_id:
            actuators.remove(actuator)
            break
    return redirect("/actuator")

