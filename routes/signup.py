from flask import Blueprint, jsonify, request
from connections import db

signup = Blueprint("signup", __name__)

auth_col = db["auth"]

@signup.route("/", methods=["GET", "POST"])
def upload_csv():

    payload = request.json

    # insert doc

    try:
        data = {
            "username": payload["username"],
            "password": payload["password_1"]
        }
        auth_col.insert_one(data)

        return jsonify({"message": "success"}), 200
    except Exception as e:

        return jsonify({"message": "failure"}), 400