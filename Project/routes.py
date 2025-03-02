from flask import render_template
from Project import app, db

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page_1")
def page_1():
    return render_template("page_1.html")

@app.route("/page_2")
def page_2():
    return render_template("page_2.html")

@app.route("/page_3")
def page_3():
    return render_template("page_3.html")