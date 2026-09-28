import pandas as pd
import joblib


def predict_activity(flow_data, model_path="models/random_forest_model.pkl"):
    """
    Predict whether a network flow is BENIGN or ATTACK.
    """

    model = joblib.load(model_path)

    prediction = model.predict(flow_data)[0]

    if prediction == 0:
        return "BENIGN"
    else:
        return "ATTACK"