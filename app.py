import os
from flask import Flask
from source.models import db, User
from blueprints import login, home, actuator, sensor, user
from werkzeug.security import generate_password_hash

def main():
    app = Flask(__name__)
    app.secret_key = "ndisanpsaiviwb2983123"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'database.db')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(login.login, url_prefix="")
    app.register_blueprint(login.logout, url_prefix="")
    app.register_blueprint(home.home, url_prefix="")
    app.register_blueprint(actuator.actuator, url_prefix="")
    app.register_blueprint(sensor.sensor, url_prefix="")
    app.register_blueprint(user.user, url_prefix="")

    app.run(port=8080, debug=True)

if __name__ == "__main__":
    main()