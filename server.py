from flask import Flask

server = Flask(__name__)

@server.route("/", methods = ["GET"])
def index():
    return "hello"

if __name__ == "__main__":
    server.run()
