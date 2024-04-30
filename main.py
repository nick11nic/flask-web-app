from flask import Flask
from blueprints import login, home, actuator, sensor


def main():
    app = Flask(__name__)

    app.register_blueprint(login.login, url_prefix="")
    app.register_blueprint(home.home, url_prefix="")
    app.register_blueprint(actuator.actuator, url_prefix="")
    app.register_blueprint(sensor.sensor, url_prefix="")

    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
