import flask
from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:
        data = json.load(f)
        return flask.jsonify(data)

@app.route('/users', methods=["POST"])
def add():
    print("Post function is executed")
    message = request.form["message"]
    port = request.form["port"]
    print("The port is ")
    print(port)
    if port == "8081":
        username = "Lender"
    else:
        username = "Borrower"
    jsonMessage = {"username": username, "message": message}
    write_json(jsonMessage)
    return "Message written to log"

def write_json(new_data, filename='users.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["log"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

if __name__ == '__main__':
    app.run("localhost", 6969, debug=True)