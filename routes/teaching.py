from flask import Blueprint, jsonify, request
import pandas as pd
teaching = Blueprint('teaching', __name__)


@teaching.route('/passpercentage', methods=['GET', 'POST'])
def passpercentage():

    """Expected JSON format
    {
    'Subject': ['Compiler', 'Green Design', 'SPM', 'Operating System', 'Cloud Computing'],
    'Pass Percentage': [76, 99, 97, 86, 82],
    'year': [1,2,2,3,3],
    'Subject Code': ['CS 201', 'CS 301', 'CS 401', 'CS 501', 'CS 601'],
    }
    """
    
    

    return 