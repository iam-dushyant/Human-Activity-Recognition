from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('models/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = pd.DataFrame([request.json])
    prediction = model.predict(data)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
