from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints import login, home, actuator, sensor, logout, user

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.secret_key = "ndisanpsaiviwb2983123"

    app.register_blueprint(login.login, url_prefix="")
    app.register_blueprint(home.home, url_prefix="")
    app.register_blueprint(actuator.actuator, url_prefix="")
    app.register_blueprint(sensor.sensor, url_prefix="")
    app.register_blueprint(logout.logout, url_prefix="")
    app.register_blueprint(user.user, url_prefix="")

    return app