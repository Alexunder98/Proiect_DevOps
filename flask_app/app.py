#!/usr/bin/python3

from flask import Flask, render_template
import requests
import json

from flask import Flask, jsonify, request

app = Flask(__name__)
result_json_list = []

def parse_json_api():
    people_from_sw = requests.get('https://swapi.dev/api/people')
    chars = people_from_sw.json()["results"]
    print(chars)
    id = 0
    for val in chars:
        result_json_list.append(
        {"id" : id,
        "Name" : val["name"], 
        "Birth Year": val["birth_year"],
        "Skin color" : val["skin_color"],
        "Hair color" : val["hair_color"],
        "Mass" : val["mass"]})
        id += 1


def get_meme():
    sr = "/ProgrammerHUmor"
    url = "https://meme-api.com/gimme" + sr
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/meme")
def meme_page():
    meme_pic, subreddit = get_meme()
    return render_template("meme.html", meme_pic=meme_pic, subreddit=subreddit)


@app.route("/chars", methods=['GET'])
def get_json():
    return result_json_list


@app.route("/chars/<int:id>", methods=['GET'])
def get_char(id):
    if id not in [char["id"] for char in result_json_list]:
        return jsonify({"status": "id is not found"}), 400
    else:
        for char in result_json_list:
            if char["id"] == id:
                return char


@app.route("/chars", methods=['POST'])
def post_char():
    # Check if body is json format
    if not request.is_json:
        return jsonify({"status": "Missing JSON in request"}), 400
    id = request.json.get('id', None)
    name = request.json.get('Name', None)
    by = request.json.get('Birth Year', None)
    sk = request.json.get('Skin color', None)
    hc = request.json.get('Hair color', None)
    mass = request.json.get('Mass', None)
    new_char = { "Name" : name, "Birth Year" : by, "Skin Color" : sk, "Hair color" : hc, "Mass" : mass, "id" : id}
    # Check if id already exists  
    if id in [char["id"] for char in result_json_list]:
        return jsonify({"status": "id is already in use"}), 400
    else:
        result_json_list.append(new_char)
        return jsonify({"id" : id}), 201


@app.route("/chars/<int:id>", methods=['PUT'])
def put_char(id):
    if not request.is_json:
        return jsonify({"status": "Missing JSON in request"}), 400
    # Update fields for choosen id
    id = request.json.get('id', None)
    name = request.json.get('Name', None)
    by = request.json.get('Birth Year', None)
    sk = request.json.get('Skin color', None)
    hc = request.json.get('Hair color', None)
    mass = request.json.get('Mass', None)
    # Check if id already exists  
    if id in [char["id"] for char in result_json_list]:
        for json in result_json_list:
            if json["id"] == id:
                json.update({ "Name" : name, "Birth Year" : by, "Skin Color" : sk, "Hair color" : hc, "Mass" : mass, "id" : id})
    else:
        result_json_list.append({ "Name" : name, "Birth Year" : by, "Skin Color" : sk, "Hair color" : hc, "Mass" : mass, "id" : id})
    return jsonify({"id" : id}), 201


@app.route("/chars/<int:id>", methods=['DELETE'])
def del_char(id):
    if not request.is_json:
        return jsonify({"status": "Missing JSON in request"}), 400
    id = request.json.get('id', None)
    if id in [char["id"] for char in result_json_list]:
        for json in result_json_list:
            if json["id"] == id:
                result_json_list.remove(json)
                return jsonify({"status" : "ok"}), 200
    else:
        return jsonify({"status" : "id not found"}), 404


@app.route("/liveness")
def liveness():
    return "\nING DevSchool 2023 Final Project LIVENESS\n"


parse_json_api()

app.run(host = "0.0.0.0", port = 80)
