from flask import Blueprint, jsonify, request
import pandas as pd
from connections import db
from math import floor

teaching = Blueprint("teaching", __name__)

teachers_col = db["teachers"]
subjects_col = db["subjects"]
endsem_pass_fail_col = db["endsem_pass_fail"]


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

    teacher_id = payload["teacher_id"]

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
        final_data['year'].append(s['year'])
        final_data['Subject Code'].append(s['subject_code'])

    return final_data


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

    print(pass_details)

    for sub in pass_details:
        sub["Pass Percentage"] = (
            sub["num_students_passed"]
            / (sub["num_students_passed"] + sub["num_students_failed"])
            * 100
        )
        sub["Pass Percentage"] = floor(sub["Pass Percentage"])

    return pass_details
