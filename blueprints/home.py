from flask import Blueprint, render_template, session, redirect, request, Response, jsonify
import paho.mqtt.client as mqtt
import threading
from datetime import date
from blueprints.user import is_admin, is_statistician, is_operator 

home = Blueprint("home", __name__, static_folder="static", template_folder="view")

values = {"Temperature": None, "Humidity": None}
messages = []

def on_message(client, userdata, message):
    global values

    old_temperature = values["Temperature"]
    old_humidity = values["Humidity"]
    
    payload = message.payload.decode()
    if "Temperature" in payload:
        if old_temperature != payload:
            values["Temperature"] = payload
            messages.insert(0, payload)

            temp = float(payload.split(":")[1])
            if temp > 50:
               print("Temperature is too high")

    elif "Humidity" in payload:
        if old_humidity != payload: 
            values["Humidity"] = payload
            messages.insert(0, payload)

            humidity = float(payload.split(":")[1])
            if humidity > 80:
                print("Humidity is too high")

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.mqttdashboard.com")
client.subscribe("flask-web-app-send")
threading.Thread(target=client.loop_forever).start()

@home.route("/", methods=["GET", "POST"])
@home.route("/home", methods=["GET", "POST"])
def home_blueprint():
    if request.method == "POST":
        command = request.form["command"]
        client.publish("flask-web-app-receive", command)
        return redirect("/")

    if "user" not in session:
        return redirect("/login")

    return render_template("home.html", values = values, messages=messages, is_admin=is_admin(), is_statistician=is_statistician(), is_operator=is_operator())

