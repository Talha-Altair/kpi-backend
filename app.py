from flask import Flask, render_template, request, jsonify
from flask_cors import CORS



app = Flask(__name__)

@app.route('/')
def index():

    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)