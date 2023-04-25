from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

from routes.teaching import teaching

app.register_blueprint(teaching, url_prefix='/teaching')

@app.route('/ping')
def index():

    return jsonify({'ping': 'Altair'})

if __name__ == '__main__':
    app.run(debug=True)