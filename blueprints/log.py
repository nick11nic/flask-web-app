from flask import Blueprint, render_template, request, redirect, session
from model.models import db, LogTemperature, LogHumidity, LogActuator
from datetime import datetime, timedelta

log = Blueprint( "log", __name__, static_folder="static", template_folder="view" )

@log.route("/log")
def log_blueprint():
    if not session.get("user"):
        return redirect("/login")
    return render_template("log.html")

@log.route('/read_logs_temperature', methods=['GET', 'POST'])
def read_logs_temperature():
    start_date_str = request.form['start_date']
    end_date_str = request.form['end_date']

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    logs = LogTemperature.query.filter(LogTemperature.timestamp >= start_date, LogTemperature.timestamp <= end_date).all()

    return render_template('log.html', sensor_data=logs)

@log.route('/read_logs_humidity', methods=['GET', 'POST'])
def read_logs_humidity():
    start_date_str = request.form['start_date']
    end_date_str = request.form['end_date']

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    logs = LogHumidity.query.filter(LogHumidity.timestamp >= start_date, LogHumidity.timestamp <= end_date).all()

    return render_template('log.html', sensor_data=logs)