from flask import Blueprint, render_template, session, redirect, request
import paho.mqtt.client as mqtt
import threading

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")


def on_message(client, userdata, message):
    messages.append(message.payload.decode())


def check_for_messages():
    client.subscribe("flask-web-app-send")
    while True:
        client.loop(timeout=0.2)


messages = []
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "flask-web-app")
client.connect("broker.mqttdashboard.com")
client.on_message = on_message
threading.Thread(target=check_for_messages).start()


@home.route("/", methods=["GET", "POST"])
@home.route("/home", methods=["GET", "POST"])
def home_blueprint():
    if request.method == "POST":
        client.publish("flask-web-app-receive", str(request.form["command"]))
        return redirect("/")

    if "user" not in session:
        return redirect("/login")

    return render_template("home.html", messages=messages)
