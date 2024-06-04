from flask import Blueprint, render_template, request, redirect, session
from source.models import db, Log
from datetime import datetime, timedelta

log = Blueprint( "log", __name__, static_folder="static", template_folder="templates" )

@log.route("/log")
def log_blueprint():
    if not session.get("user"):
        return redirect("/login")
    return render_template("log.html")

@log.route('/read_logs', methods=['GET', 'POST'])
def read_logs():
    start_date_str = request.form['start_date']
    end_date_str = request.form['end_date']

    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    logs = Log.query.filter(Log.timestamp >= start_date, Log.timestamp <= end_date).all()

    return render_template('log.html', sensor_data=logs)