import json
from flask import Flask, jsonify, request, render_template
import anaylze
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(anaylze.getInfo())

@app.route('/api', methods=['GET'])
def api():
    # return the link of the string submitted from the form
    return jsonify(request.form.get('url'))

@app.route('/')
def index():
    return render_template('index.html')