from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "James")

@views.route("/home")
def home2():
    return render_template("index1.html")

