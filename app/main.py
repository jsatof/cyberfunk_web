from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import psycopg2
import os

app = Flask(__name__)

database = SQLAlchemy(app)

class Users(database.Model):
    __tablename__ = "Users"
    userid = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(32), unique = True)
    password = database.Column(database.String(16), unique = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

connection = psycopg2.connect(DATABASE_URL, sslmode = "require")

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "" or password == "":
            return render_template("login.html", message = "Please Enter Required Fields")


if __name__ == "__main__":
    app.run()
