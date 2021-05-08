from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

sitings = ["home", "school", "park"]

@app.route('/')
def hello_world():
  ms_num = datetime.now().microsecond
  return render_template('index.html', ms_num=ms_num, sitings=sitings)

@app.route('/api/records')
def api_records():
  return jsonify(sitings)

@app.route('/api/records', methods=['POST'])
def create_records():
  location = request.json['location']
  sitings.append(location)
  return "", 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True, extra_files=['templates/index.html', 'static/css/styles.css', 'static/js/main.js', 'static/img/delete.png'])