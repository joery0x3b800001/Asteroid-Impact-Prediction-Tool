from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load the model
model_path = 'models/model.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({'error': 'Model not found. Please train the model first.'}), 500

    data = request.json
    required_features = ['absolute_magnitude_h', 'diameter_max_km', 'velocity_km_s', 'miss_distance_km', 'diameter_min_km']
    
    # Check if all required features are in the input data
    if not all(feature in data for feature in required_features):
        return jsonify({'error': 'Missing required features in input data'}), 400

    try:
        # Create a DataFrame from the input data
        df = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(df)
        is_hazardous = bool(prediction[0])
        
        return jsonify({'is_potentially_hazardous_asteroid': is_hazardous})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
