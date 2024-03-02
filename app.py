import json
from flask import Flask, jsonify, request
import anaylze
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(anaylze.getInfo())