from flask import Blueprint, redirect, url_for, render_template, request, url_for

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        fname = request.form["fname"].lower()
        lname = request.form["lname"].lower()
        return redirect(url_for("auth.user", fname=fname))
    else:
        return render_template("login.html")

@auth.route("/<fname>")
def user(fname):
    return f"<h1>{fname}</h1>"