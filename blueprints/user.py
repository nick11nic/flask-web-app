from flask import Blueprint, render_template, session, redirect, request, flash

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")

users = [
    {"id": 1, "email": "user@gmail.com", "password": "123"},
    {"id": 2, "email": "adm@gmail.com", "password": "123"}
]

@user.route("/user")
def user_blueprint():
    if session.get("username") == "adm":
        return render_template("user.html", users=users)
    return redirect("/home")

@user.route("/create_user", methods=["POST"])
def create_user():
    global users
    email = request.form.get("email")
    password = request.form.get("password")
    user_id = len(users) + 1 
    new_user = {"id": user_id, "email": email, "password": password}
    users.append(new_user)
    return redirect("/user")

@user.route("/edit_user", methods=["POST"])
def edit_user():
    global users
    user_id = int(request.form.get("edit_user_id"))
    new_email = request.form.get("new_email")
    new_password = request.form.get("new_password")

    user_found = False
    for user in users:
        if user["id"] == user_id:
            user_found = True
            if new_email:
                user["email"] = new_email
            if new_password:
                user["password"] = new_password
            break
        
    if not user_found:
        flash("User not found.")
        return redirect("/user")

    return redirect("/user")


@user.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    global users
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            break
    return redirect("/user")
