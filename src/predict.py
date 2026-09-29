import pandas as pd
import joblib


def predict_activity(flow_data, model_path="models/random_forest_model.pkl"):
    """
    Predict whether a network flow is BENIGN or ATTACK.

    Parameters:
        flow_data: Pandas DataFrame containing network traffic features.
        model_path: Path to the trained Random Forest model.

    Returns:
        BENIGN or ATTACK
    """

    model = joblib.load(model_path)

    prediction = model.predict(flow_data)[0]

    if prediction == 0:
        return "BENIGN"
    else:
        return "ATTACK"


if __name__ == "__main__":
    print("Suspicious Activity Detector")
    print("============================")
    print()
    print("Prediction function loaded successfully.")
    print("The trained Random Forest model is ready for prediction.")