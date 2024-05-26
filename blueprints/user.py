from flask import Blueprint, render_template, session, redirect, request, flash
from source.models import db, User
from werkzeug.security import generate_password_hash

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")

@user.route("/user")
def user_blueprint():
    if session.get("role") == "admin":
        return render_template("user.html", users=read_users())
    return redirect("/home")

@user.route("/create_user", methods=["POST"])
def create_user():
     email = request.form.get("email")
     password = request.form.get("password")
     hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
     user = email.split("@")[0]
     new_user = User(username=user, email=email, password=hashed_password, role="user")
     db.session.add(new_user)
     db.session.commit()
     return redirect("/user")

@user.route("/read_users")
def read_users():
    users = User.query.all()
    return users

@user.route("/edit_user", methods=["POST"])
def edit_user():
    user_id = int(request.form.get("edit_user_id"))
    new_email = request.form.get("new_email")
    new_password = request.form.get("new_password")

    user = User.query.filter_by(id=user_id).first()

    if user:
        if new_email:
            user.email = new_email
        if new_password:
            hashed_password = generate_password_hash(new_password, method="pbkdf2:sha256")
            user.password = hashed_password
        db.session.commit()
    else:
        flash("User not found.", "warning")

    return redirect("/user")


@user.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        if user.username != "adm":
            db.session.delete(user)
            db.session.commit()
        else:
            flash("Cannot delete admin.", "error")
    return redirect("/user")
