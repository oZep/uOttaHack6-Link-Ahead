import json
from flask import Flask, jsonify, request, render_template
import anaylze
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(anaylze.getInfo())


@app.route('/')
def index():
    return render_template('index.html')