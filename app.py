from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def index():
    return "Random Forest Prediction API (POST-based) is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract and validate all required features
        features = [
           float(data['gender']),
            float(data['age']),
            float(data['hypertension']),
            float(data['heart_disease']),
            float(data['avg_glucose_level']),
            float(data['smoking_status'])
        ]
    except (KeyError, TypeError, ValueError) as e:
        return jsonify({
            "error": "Missing or invalid input. Required fields: age, hypertension, avg_glucose_level, bmi, heart_disease, gender.",
            "details": str(e)
        }), 400

    prediction = model.predict([features])[0]
    proba = model.predict_proba([features])[0].tolist()

    return jsonify({
        "prediction": int(prediction),
        "probabilities": {
            "class_0": proba[0],
            "class_1": proba[1]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
