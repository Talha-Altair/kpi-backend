from flask import Blueprint, jsonify, request
import pandas as pd
from connections import db
import io
import json

uploader = Blueprint("uploader", __name__)

dashboard_col = db["dashboard"]

@uploader.route("/", methods=["GET", "POST"])
def upload_csv():

    payload = request.json

    username = payload["username"]

    payload = payload["data"]

    payload["username"] = username

    payload['basic']['name'] = username

    payload['basic']['email'] = username + "@crescent.education"

    try:

        dashboard_col.insert_one(payload)

        return jsonify({"message": "success"}), 200
    
    except Exception as e:
            
        return jsonify({"message": "failure"}), 400
