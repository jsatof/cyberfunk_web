from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
import psycopg2
import os

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


# Database Functions

def create_tables(connection): # assuming connection is working

    # append commands when want to create more tables on init
    commands = (
        """
        CREATE TABLE users (
            uid SERIAL PRIMARY KEY,
            username VARCHAR(16) NOT NULL,
            password VARCHAR(16) NOT NULL
        )
        """)

    

    try:
        params = config()

        cursor = connection.cursor()

        for command in commands:
            cursor.execute(command)

        cursor.close()
        connection.commit()
    
    except(Exception. psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    create_tables()
import psycopg2

def user_lookup(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT uid, username, password FROM users ORDER BY uid"

        cursor.execute(query)

        matches = []        

        row = cursor.fetchone()

        cursor.close()



    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    app.run()
