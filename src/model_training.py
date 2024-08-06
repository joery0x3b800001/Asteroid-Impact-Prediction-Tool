from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

def train_model(df):
    X = df[['absolute_magnitude_h', 'diameter_max_km', 'velocity_km_s', 'miss_distance_km', 'diameter_min_km']]  # Example features
    y = df['is_potentially_hazardous_asteroid']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return model, accuracy, report

# Assuming you have a function that retrieves data
# df = pd.read_csv('../resources/data.csv')
# _, acc, _ = train_model(df)

# print(acc)

# from joblib import dump, load

# Serialize
# dump(model, 'model.joblib')

# Deserialize
# model = load('model.joblib')