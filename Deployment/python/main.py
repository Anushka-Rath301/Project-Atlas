from arduino.app_utils import App, Bridge
import pandas as pd
from inference import predict
from datetime import datetime
from pathlib import Path
import os

def rec_values(voltage, current, vibration, tempC):
    print("REC_VALUES CALLED", flush=True)
    features = [voltage, current, vibration, tempC]
    time=datetime.now().strftime("%H:%M:%S")
    result,confidence = predict(features)
    features.append(result)
    features.append(confidence)
    features.insert(0,time)
    new_row = pd.DataFrame(
    [features], columns=["Time","Voltage","Current","Vibration","Temperature","Health Status","Confidence"])

    csv_file = Path(__file__).resolve().parent / "sensor_log.csv"

    print(os.getcwd())
    print(os.path.abspath(csv_file))

    if os.path.exists(csv_file):
        print(new_row)
        new_row.to_csv(csv_file, mode="a", header=False, index=False)
    else:
        print(new_row)
        new_row.to_csv(csv_file, mode="w", header=True, index=False)

    return str(result)
print("MAIN.PY LOADED", flush=True)
Bridge.provide("rec_values", rec_values)

App.run()