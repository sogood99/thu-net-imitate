from flask import Flask, request
from flask_cors import CORS
from db import *
from random import randint, random

app = Flask(__name__)
CORS(app)

@app.route("/get", methods = ['POST'])
def get_user():
    data = request.get_json()
    user = data['username']
    password = data['password']
    return check_and_add(user, password, randint(0, 5) + random())

if __name__ == "__main__":
    app.run(host='localhost',port='5000',debug=True)