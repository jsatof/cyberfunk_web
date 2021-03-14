from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/post", methods = ["POST"])
def post():
    if request.json:
        return request.json

    return "bad request"

if __name__ == "__main__":
    app.run()
