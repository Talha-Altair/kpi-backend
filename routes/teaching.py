from flask import Blueprint, jsonify, request
import pandas as pd
from connections import db
from math import floor

teaching = Blueprint("teaching", __name__)

teachers_col = db["teachers"]
subjects_col = db["subjects"]
endsem_pass_fail_col = db["endsem_pass_fail"]

@teaching.route("/add", methods=["GET", "POST"])
def add():

    payload = request.json

    payload['subject_codes'] = []

    teacher_id = int(payload["teacher_id"])

    teacher_data = teachers_col.find_one({"teacher_id": teacher_id})

    if teacher_data:
        return jsonify({"message": "Teacher already exists!"}), 400

    teachers_col.insert_one(payload)

    return jsonify({"message": "Teacher added successfully!"}), 200

@teaching.route("/add_pass_fail", methods=["GET", "POST"])
def add_pass_fail():

    payload = request.json

    subject_code = payload["subject_code"]

    payload['num_students_passed'] = int(payload['num_students_passed'])
    payload['num_students_failed'] = int(payload['num_students_failed'])

    subject_data = subjects_col.find_one({"subject_code": subject_code})

    if not subject_data:
        
        return jsonify({"message": "Subject does not exist!"})

    endsem_pass_fail_col.insert_one(payload)

    return jsonify({"message": "Pass fail data added successfully!"})

@teaching.route("/addsubjects", methods=["GET", "POST"])
def addsubjects():

    payload = request.json

    subject_data = subjects_col.find_one({"subject_code": payload['subject_code']})

    teacher_id = int(payload["teacher_id"])

    teacher_data = teachers_col.find_one({"teacher_id": teacher_id})

    if not teacher_data:

        return jsonify({"message": "Teacher does not exist!"})
    
    teachers_col.update_one({"teacher_id": teacher_id}, {"$push": {"subject_codes": payload['subject_code']}})

    if subject_data:

        return jsonify({"message": "Subject already exists!"})

    subjects_col.insert_one(payload)

    return jsonify({"message": "Subject added successfully!"})


@teaching.route("/passpercentage", methods=["GET", "POST"])
def passpercentage():
    """Expected JSON format
    {
    'Subject': ['Compiler', 'Green Design', 'SPM', 'Operating System', 'Cloud Computing'],
    'Pass Percentage': [76, 99, 97, 86, 82],
    'year': [1,2,2,3,3],
    'Subject Code': ['CS 201', 'CS 301', 'CS 401', 'CS 501', 'CS 601'],
    }
    """

    payload = request.json

    teacher_id = int(payload["teacher_id"])

    teacher_data = teachers_col.find_one({"teacher_id": teacher_id})

    subject_codes = teacher_data["subject_codes"]

    subject_details = get_subject_details(subject_codes)

    pass_details = get_pass_details(subject_codes)

    final_data = {
        "Subject": [],
        "Pass Percentage": [],
        "year": [],
        "Subject Code": []
    }

    for p,s in zip(pass_details, subject_details):

        final_data['Subject'].append(s['subject_name'])
        final_data['Pass Percentage'].append(p['Pass Percentage'])
        final_data['year'].append(int(s['year']))
        final_data['Subject Code'].append(s['subject_code'])

    return jsonify(final_data)


def get_subject_details(subject_codes):
    subject_details = []

    for subject_code in subject_codes:
        try:
            subject_data = subjects_col.find_one(
                {"subject_code": subject_code}, {"_id": 0}
            )
        except:
            subject_data = "Subject not found"

        subject_details.append(subject_data)

    return subject_details


def get_pass_details(subject_codes):
    
    pass_details = []

    for subject_code in subject_codes:
        try:
            subject_data = endsem_pass_fail_col.find_one(
                {"subject_code": subject_code}, {"_id": 0}
            )
        except:
            subject_data = "Subject not found"

        pass_details.append(subject_data)

    for sub in pass_details:
        sub["Pass Percentage"] = (
            sub["num_students_passed"]
            / (sub["num_students_passed"] + sub["num_students_failed"])
            * 100
        )
        sub["Pass Percentage"] = floor(sub["Pass Percentage"])

    return pass_details
