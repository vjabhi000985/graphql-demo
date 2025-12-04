# model.py
import joblib
from sklearn.linear_model import LinearRegression
import numpy as np
import os

MODEL_PATH = "model.pkl"

def load_or_train_model():
    # If model already exists, load it
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    # Fake training data (sqft → price)
    X = np.array([[500], [800], [1000], [1200], [1500]])
    y = np.array([30, 50, 70, 85, 110])  # fake price

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    return model

model = load_or_train_model()

def predict_price(sqft: float) -> float:
    return float(model.predict([[sqft]])[0])