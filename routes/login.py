from flask import Blueprint, jsonify, request
from connections import db

login = Blueprint("login", __name__)

auth_col = db["auth"]

@login.route("/", methods=["GET", "POST"])
def upload_csv():

    payload = request.json

    try:
        user_data = auth_col.find_one({"username": payload["username"]})
        
        if user_data["password"] == payload["password"]:

            return jsonify({"message": "success"}), 200
        
        return jsonify({"message": "Unauthorized"}), 400
    
    except Exception as e:

        return jsonify({"message": "failure"}), 400