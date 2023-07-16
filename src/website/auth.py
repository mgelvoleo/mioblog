from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

auth = Blueprint("auth", __name__)

auth.permanent_session_lifetime = timedelta(minutes=5)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True

        fname = request.form["fname"].lower()
        lname = request.form["lname"].lower()

        session["fname"] = fname
        session["lname"] = lname

        flash("Login Successful!")

        return redirect(url_for("auth.user"))
    else:
        if "fname" in session:
            flash("Already Logged In!")
            return redirect(url_for("auth.user"))

        return render_template("login.html")

@auth.route("/logout")
def logout():
    flash(f"You have been logged out", "info")
    session.pop("fname", None)
    return redirect(url_for("auth.login"))

@auth.route("/user")
def user():
    if "fname" in session:
        fname = session["fname"]
        flash(f"Welcome, {fname}!", "info")
        return render_template("user.html", fname=fname)
    else:
        flash("You are not logged in")
        return redirect(url_for("auth.login"))
