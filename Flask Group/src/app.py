import json
import flask
from flask import Flask, request
import os
from reset_data import reset
import uuid
from datetime import datetime

####################
### This block initializes the arrays "Users" and "Pleets" from the json file storage system
### To edit any data, just edit these arrays, and call the update() method
####################

Users = []
Pleets = []

here = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(here, "data.json")

with open(data,"r", encoding='utf-8') as datafile:
    rawdata = json.load(datafile)
    Users = rawdata["users"]
    Pleets = rawdata["pleets"]

def update():
    with open(data,"w", encoding='utf-8') as datafile:
        json.dump({
            "users": Users,
            "pleets": Pleets
        }, datafile)

####################
### Flask work starts here
### A Hello World method has been provided as starter, and can be replaced
####################

app = Flask(__name__)

# Testing purposes
@app.route("/reset", methods=["POST"])
def reset_data():
    global Users, Pleets
    reset()
    with open(data,"r", encoding='utf-8') as datafile:
        rawdata = json.load(datafile)
        Users = rawdata["users"]
        Pleets = rawdata["pleets"]
    return {"success": True}


# Pleets is array of pleets
# _id is the key with the pleet id
# Pleets[i]['_id'] == pleet_id
# flask.Response(body, status=200)
# json.dumps() -- converts python dictionary to json format

# GET pleet from pleet_id
@app.route("/pleets/<pleet_id>", methods=["GET"])
def get_pleet(pleet_id):
    for pleet in Pleets:
        if pleet['_id'] == pleet_id:
            return flask.Response(json.dumps(pleet), status=200)
    return flask.Response(json.dumps({"message": "User not found!"}), status=404)

# GET top 10 recent pleets
@app.route("/pleets", methods=["GET"])
def top_10_pleets():
    # arr = []
    # for i in range(0, min(10, len(Pleets))):
    #     arr.append(Pleets[i])
    # return flask.Response(json.dumps({"pleets": arr}), status=200)
    return {'pleets': Pleets[:10]}, 200
    return flask.Response(json.dumps({"pleets": Pleets[:10]}), status=200)

# GET all pleets from a user
@app.route("/users/<user_id>/pleets", methods=["GET"])
def get_all_pleets(user_id):
    pleets_arr = [p for p in Pleets if p["user_id"] == user_id]
    if pleets_arr:
        return flask.Response(json.dumps({"pleets": pleets_arr}), status=200)
    return flask.Response(json.dumps({"message": "User not found!"}), status=404)


# request.form.get('username')
# str(uuid.uuid4()) -- make a new id
# from datetime import datetime
# datetime.now().time()

# POST make a new pleet
# not tested yet
@app.route("/pleets", methods=["POST"])
def make_new_pleet():
    username = request.form.get('username')
    text = request.form.get('text')
    user_id = None
    for user in Users:
        if user['username'] == username:
            user_id = user['_id']
    if user_id is not None:
        Pleets.append({"_id": str(uuid.uuid4()), "datetime": datetime.now().time(), "text": text, "user_id": user_id})
        update()
        return flask.Response(json.dumps({"message": "Pleet successfully added!", "pleet_id": str(uuid.uuid4())}), status=200)
    return flask.Response(json.dumps({"message": "User not found!"}), status=404)

# DELETE a pleet
# to be tested later
@app.route("/pleets/<pleet_id>", methods=["DELETE"])
def delete_pleet(pleet_id):
    removed = None
    for pleet in Pleets:
        if pleet['_id'] == pleet_id:
            removed = Pleets.pop(pleet)
    if removed is not None:
        update()
        return flask.Response(json.dumps({"message": "Pleet successfully deleted!"}), status=200)
    return flask.Response(json.dumps({"message": "User not found!"}), status=404)

# PUT edit profile
# to be tested later
@app.route("/user/<user_id>", methods=["PUT"])
def edit_profile(user_id):
    display_name = request.form.get('display name')
    for user in Users:
        if user['_id'] == user_id:
            user['display_name'] = display_name
            update()
            return flask.Response(json.dumps({"message": "User Profile Successfully edited!"}), status=200)
    return flask.Response(json.dumps({"message": "User not found!"}), status=404)

@app.route("/")
def hello_world():
    return {'data': 'Hello World'}

app.run(debug=True, port=5001)
