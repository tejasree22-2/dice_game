from flask import Flask, jsonify
from flask_cors import CORS
from backend.dice import roll, get_face

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/roll', methods=['GET'])
def roll_dice():
    result = roll()
    return jsonify({
        "number": result,
        "face": get_face(result)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
