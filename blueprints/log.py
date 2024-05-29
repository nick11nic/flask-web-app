from flask import Blueprint, render_template, request, redirect, session, flash
from blueprints.user import is_admin, is_statistician

log = Blueprint( "log", __name__, static_folder="static", template_folder="templates" )

@log.route("/log")
def log_blueprint():
    if not session.get("user"):
        return redirect("/login")
    return render_template("log.html")

