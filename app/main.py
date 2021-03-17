from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import psycopg2
import os

import create_tables

app = Flask(__name__)
api = Api(app)

DATABASE_URL = os.environ["DATABASE_URL"]
connection = psycopg2.connect(DATABASE_URL, sslmode = "require")
create_tables(connection)

parser = reqparse.RequestParser()

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

# API Routes are below
class Login(Resource):
    def post(self):
        args = parser.parse_args()
        
        # STUB: check for valid args

        uname = args["username"]
        pword = args["password"]



app.add_resource(Login, "/api/login")

if __name__ == "__main__":
    app.run()
