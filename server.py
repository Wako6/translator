from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from translate import Translate

# Initialize variables for the API
app = Flask(__name__)
cors = CORS(app)
translator = Translate()

@app.route("/frtoen", methods=["GET"])
@cross_origin()
def inEnglish():
    """Translate french in english."""
    sentence = request.args.get('sentence', '')
    sentence = translator.translate_fr_to_en(sentence)

    return jsonify(sentence)

@app.route("/entofr", methods=["GET"])
@cross_origin()
def inFrench():
    """Translate english in french."""
    sentence = request.args.get('sentence', '')
    sentence = translator.translate_en_to_fr(sentence)

    return jsonify(sentence)

if __name__ == '__main__':
    # Launch the server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )