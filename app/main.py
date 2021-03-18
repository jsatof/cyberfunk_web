from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
import psycopg2
import os

app = Flask(__name__)
api = Api(app)

#DATABASE_URL = os.environ["DATABASE_URL"]
#connection = psycopg2.connect(DATABASE_URL, sslmode = "require")

parser = reqparse.RequestParser()

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

# API Routes are below
class Login(Resource):
    def post(self):
        json_data = request.get_json(force = True)
        
        # STUB: check for valid args

        uname = json_data["username"]
        pword = json_data["password"]

        return jsonify(userame = uname, password = pword)

api.add_resource(Login, "/api/login")

if __name__ == "__main__":
    app.run()
