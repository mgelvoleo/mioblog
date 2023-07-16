from flask import Blueprint, redirect, url_for, render_template, request, url_for

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("index.html")


@views.route("/blog")
def blog():
    return render_template("blog.html")


@views.route("/project")
def project():
    return render_template("project.html")