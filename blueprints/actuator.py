from flask import Blueprint, render_template, redirect, request, session
from blueprints.user import is_admin
from source.models import db, Actuator

actuator = Blueprint("actuator", __name__, static_folder="static", template_folder="templates")

@actuator.route("/actuator")
def actuator_blueprint():
    if "user" not in session:
        return redirect("/login")

    return render_template("actuator.html", actuators=read_actuators())

@actuator.route("/create_actuator", methods=["POST"])
def create_actuator():
    if not is_admin():
        session.clear()
        return redirect("/home")
    name = request.form.get("name")
    type = request.form.get("type")
    value = request.form.get("value")

    new_actuator = Actuator(name = name, type = type, value = value)
    db.session.add(new_actuator)
    db.session.commit()

    return redirect("/actuator")

@actuator.route("/read_actuators")
def read_actuators():
    actuators = Actuator.query.all()
    return actuators

@actuator.route("/delete_actuator/<int:actuator_id>", methods=["POST"])
def delete_actuator(actuator_id):
    if not is_admin():
        session.clear()
        return redirect("/home")
    actuator = Actuator.query.filter_by(id=actuator_id).first()
    if actuator:
        db.session.delete(actuator)
        db.session.commit()
    return redirect("/actuator")

