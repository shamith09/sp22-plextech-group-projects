from flask import Flask, request
from flask_cors import CORS

import os
import json
import uuid
import time
from reset_data import reset


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
CORS(app)

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
# dictionary[new_key] = dictionary.pop(old_key)
# dictionary_copy = dictionary.copy()

# GET pleet from pleet_id
@app.route("/pleets/<pleet_id>", methods=["GET"])
def get_pleet(pleet_id):
    for pleet in Pleets:
        if pleet['_id'] == pleet_id:
            for u in Users: 
                if u["_id"] == pleet["user_id"]:
                    user_copy = u.copy()
                    user_copy['user_id'] = user_copy.pop('_id')
                    print(u)

            result = {
                "pleet_id": pleet['_id'],
                "user": user_copy,
                "text": pleet['text'],
                "datetime": pleet['datetime']
            }
            return result, 200
    return {"message": "User not found!"}, 404

# GET top 10 recent pleets
@app.route("/pleets", methods=["GET"])
def top_10_pleets():
    # arr = []
    # for i in range(0, min(10, len(Pleets))):
    #     arr.append(Pleets[i])
    # return flask.Response(json.dumps({"pleets": arr}), status=200)
    result_list = []
    for pleet in Pleets[:10]:
        for u in Users: 
            if u["_id"] == pleet["user_id"]:
                user_copy = u.copy()
                user_copy['user_id'] = user_copy.pop('_id')
        result = {
            "pleet_id": pleet['_id'],
            "user": user_copy,
            "text": pleet['text'],
            "datetime": pleet['datetime']
        }
        result_list.append(result)
    return {'pleets': result_list}, 200

# GET all pleets from a user
@app.route("/users/<user_id>/pleets", methods=["GET"])
def get_all_pleets(user_id):
    result_list = []
    pleets_arr = [p for p in Pleets if p["user_id"] == user_id]
    for u in Users: 
        if u["_id"] == user_id:
            user_copy = u.copy()
            user_copy['user_id'] = user_copy.pop('_id')
    for pleet in pleets_arr:
        result = {
            "pleet_id": pleet['_id'],
            "user": user_copy,
            "text": pleet['text'],
            "datetime": pleet['datetime']
        }
        result_list.append(result)
    if pleets_arr:
        return {'pleets': result_list}, 200

    return {"message": "User not found!"}, 404


# request.form.get('username')
# str(uuid.uuid4()) -- make a new id
# import time
# time.ctime()

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
        id = str(uuid.uuid4())
        Pleets.append({"_id": id, "datetime": time.time(), "text": text, "user_id": user_id})
        update()
        return {"message": "Pleet successfully added!", "pleet_id": id}, 200
    return {"message": "User not found!"}, 404

# DELETE a pleet
# to be tested later
@app.route("/pleets/<pleet_id>", methods=["DELETE"])
def delete_pleet(pleet_id):
    removed = None
    for i in range(len(Pleets)):
        if Pleets[i]['_id'] == pleet_id:
            removed = Pleets.pop(i)
    if removed is not None:
        update()
        return {"message": "Pleet successfully deleted!"}, 200
    return {"message": "User not found!"}, 404

# PUT edit profile
# to be tested later
@app.route("/users/<user_id>", methods=["PUT"])
def edit_profile(user_id):
    display_name = request.form.get('display name')
    for i in range(len(Users)):
        if Users[i]['_id'] == user_id:
            # removed = Users.pop(i)
            Users[i]['display name'] = display_name
            # Users.append(remov
            update()
            return {"message": "User Profile Successfully edited!"}, 200
    return {"message": "User not found!"}, 404

@app.route("/")
def hello_world():
    return {'data': 'Hello World'}

app.run(port=5001)