from flask import Flask, request, jsonify
from model import predict_probability

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    probability = predict_probability(data["age"], data["purchase_amount"])
    return jsonify({"probability": probability})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)