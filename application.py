from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s/cyberfunk.db" % os.getcwd()
db = SQLAlchemy(application)

class Score(db.Model):
    sid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    score = db.Column(db.Integer)
    max_combo = db.Column(db.Integer)
    accuracy = db.Column(db.Float)
    grade = db.Column(db.String)

@application.route("/")
def index():
    dbcon = sqlite3.connect("cyberfunk.db")
    dbcon.row_factory = sqlite3.Row

    cursor = dbcon.cursor()
    cursor.execute("select * from score order by sid desc")

    rows = cursor.fetchall()

    return render_template("index.html", rows = rows)

@application.route("/submit_score", methods = ["POST"])
def submit_score():
    if request.method == "POST":
        print(request.json)
        
        dbconn = sqlite3.connect("cyberfunk.db")

        username = request.json["username"]
        grade = request.json["grade"]
        score = request.json["score"]
        accuracy = request.json["accuracy"]
        max_combo = request.json["max_combo"]

        cursor = dbconn.cursor()
        cursor.execute("insert into score (username, grade, score, max_combo, accuracy) values (?,?,?,?,?)", (username, grade, score, max_combo, accuracy))

        dbconn.commit()
        dbconn.close()

        return {"response": 201}

    else:
        return {"response": 402}


if __name__ == "__main__":
    application.run()
