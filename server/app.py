from flask import Flask, request
from flask_cors import CORS
from db import *
from random import randint, random

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def test():
    """
    Check if backend successfully started
    """
    return "<h1>Success</h1>"

@app.route("/get", methods = ['POST'])
def get_user():
    """
    Attempt to login, if username doesnt match password then return dict with None
    """
    data = request.get_json()
    if (not data):
        return
    user = data.get('username',None)
    password = data.get('password',None)
    return check_and_send(user, password)

@app.route("/logout", methods=['POST'])
def logout():
    """
    Logout and add random value to user
    """
    data = request.get_json()
    if (not data):
        return
    user = data.get('username',None)
    return add_usage(user, randint(0, 5) + random())

if __name__ == "__main__":
    app.run(host='localhost',port='5000',debug=True)