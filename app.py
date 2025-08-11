from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask Backend!", "data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
