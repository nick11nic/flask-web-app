from flask import Blueprint, render_template, request, redirect, session
from datetime import datetime, timedelta

log = Blueprint( "log", __name__, static_folder="static", template_folder="templates" )

@log.route("/log")
def log_blueprint():
    if not session.get("user"):
        return redirect("/login")
    return render_template("log.html")

def get_sensor_data(start_date, end_date):
    return [
        {"sensor": "Sensor 1", "value": 23, "timestamp": start_date},
        {"sensor": "Sensor 2", "value": 25, "timestamp": start_date},
        {"sensor": "Sensor 3", "value": 22, "timestamp": end_date},
    ]

@log.route('/read_logs', methods=['GET', 'POST'])
def read_logs():
    if request.method == 'POST':
        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        sensor_data = get_sensor_data(start_date, end_date)
    else:
        sensor_data = []

    return render_template('log.html', sensor_data=sensor_data)