from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/medicalrecord', methods=['POST'])
def add_medical_record():
    data = request.get_json()
    return jsonify({"status": "Record added"}), 201

@app.route('/medicalrecord', methods=['GET'])
def get_medical_record():
    return jsonify({"status": "Record fetched"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
