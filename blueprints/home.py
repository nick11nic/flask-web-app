from flask import Flask, Blueprint, render_template, session, redirect, request, Response, jsonify
import paho.mqtt.client as mqtt
import threading
from datetime import date
from blueprints.user import is_admin, is_statistician, is_operator
from source.models import db, Log

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

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

            temp = int(payload.split(":")[1])
            if temp > 50:
                log = Log(name = "Temperature", value = temp, timestamp = date.today())
                db.session.add(log)
                db.session.commit()


    elif "Humidity" in payload:
        if old_humidity != payload: 
            values["Humidity"] = payload
            messages.insert(0, payload)

            humidity = int(payload.split(":")[1])
            if humidity > 50:
                log = Log(name = "Humidity", value = humidity, timestamp = date.today())
                db.session.add(log)
                db.session.commit()

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
