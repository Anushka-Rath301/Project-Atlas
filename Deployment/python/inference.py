from pathlib import Path
import joblib
import pandas as pd


MODEL_PATH = Path(__file__).resolve().parent / "motor_health_model.pkl"
model = joblib.load(MODEL_PATH)

def predict(features):
    X = pd.DataFrame(
        [features],
        columns=["Voltage","Current","Vibration", "Temperature"])

    prediction= model.predict(X)[0]
    prob = model.predict_proba(X)
    classes = model.classes_

    index = list(classes).index(prediction)
    confidence = round(prob[0][index]*100, 2)


    return prediction,confidence