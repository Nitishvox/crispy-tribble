from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load your trained model
MODEL_PATH = "models/content/strategy-bert"

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

# Serve the index.html file properly
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict_strategy():
    data = request.json
    text = data.get("input_text", "")

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    output = model(**inputs).logits
    prediction = torch.argmax(output).item()
    strategy = "Pit Now" if prediction == 1 else "Hold Position"

    return jsonify({"strategy": strategy})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
