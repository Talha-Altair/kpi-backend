from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from settings import PORT, HOST

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

from routes.teaching import teaching
from routes.upload import uploader
from routes.login import login
from routes.signup import signup
from routes.dashboard import dashboard

app.register_blueprint(teaching, url_prefix='/teaching')
app.register_blueprint(uploader, url_prefix='/upload')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(signup, url_prefix='/signup')
app.register_blueprint(dashboard, url_prefix='/dashboard')

@app.route('/ping')
def index():

    return jsonify({'ping': 'Altair'})

if __name__ == '__main__':

    app.run(debug=True, host=HOST, port=PORT)