from flask import Blueprint, redirect, url_for, render_template, request, url_for, session
from datetime import timedelta

auth = Blueprint("auth", __name__)

auth.permanent_sessions_lifetime =  timedelta(minutes=5)


@auth.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":

        session.permanent = True

        fname = request.form["fname"].lower()
        lname = request.form["lname"].lower()


        session["fname"] = fname 
        session["lname"] = lname

        return redirect(url_for("auth.user"))
    else:
        if "fname" in session:
            return redirect(url_for("auth.user"))
        
        return render_template("login.html")
    
@auth.route("/logout")
def logout():
    session.pop("fname", None)
    return redirect(url_for("auth.login"))

@auth.route("/user")
def user():
    if "fname" in session:
        fname = session["fname"]
        return f"<h1>{fname}</h1>"
    else: 
        return redirect(url_for("auth.login"))