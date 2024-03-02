import json
from compute_sketch_factor import compute_sketch_factor
from flask import Flask, jsonify, redirect, request, render_template, url_for
import anaylze
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(anaylze.getInfo())

@app.route('/api', methods=['POST'])
def api():
    url = request.form.get('url')
    if url:
        sketch_factor = compute_sketch_factor(url)
        return redirect(url_for('index') + '?value='+str(sketch_factor))
    else:
        return jsonify({'error': 'No URL provided'}), 400

@app.route('/')
def index():
    return render_template('index.html')