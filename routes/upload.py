from flask import Blueprint, jsonify, request
import pandas as pd
from connections import db
import io

uploader = Blueprint("uploader", __name__)

teachers_col = db["teachers"]
subjects_col = db["subjects"]
endsem_pass_fail_col = db["endsem_pass_fail"]

@uploader.route("/", methods=["GET", "POST"])
def upload_csv():

    payload = request.json

    if payload["name"] == "teachers":

        col = teachers_col

    json_data = pd.read_csv(io.StringIO(payload["file"]), encoding="utf-8", sep=",")

    json_data = json_data.to_dict(orient="records")

    for data in json_data:

        data["subject_codes"] = []

    col.insert_many(json_data)

    return jsonify({"message": "success"}), 200