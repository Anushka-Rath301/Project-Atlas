# Project Atlas

## Edge AI-based Predictive Maintenance and Health Monitoring System for Small Electrical Machines
Project Atlas is an Edge AI solution developed to monitor the health of small electrical machines in real time using the Arduino UNO Q. The system continuously acquires voltage, current, temperature and vibration data, performs local AI inference using a trained Random Forest model, and predicts the health condition of the machine before severe failures occur.

The acquired sensor data and prediction results are logged into CSV files and visualized through a Streamlit-based analytics dashboard. The dashboard provides real-time monitoring, historical trends, health score, maintenance recommendations and automatic email alerts whenever a faulty condition is detected.

## Objectives

* Real-time health monitoring
* Predictive maintenance using Edge AI
* Local AI inference on Arduino UNO Q
* Cloud connectivity via Wi-Fi/MQTT
* Interactive analytics dashboard
* Maintenance recommendations based on historical trends

## Tech Stack

### Hardware
- Arduino UNO Q
- ZMPT101B Voltage Sensor
- WCS1700 Current Sensor
- DS18B20 Temperature Probe Sensor
- MPU6050 Vibration Sensor

The following figure shows the complete hardware implementation of Project Atlas, including the motor-side sensor placement and controller-side interfacing.
<img width="1080" height="1350" alt="Hardware_overview" src="https://github.com/user-attachments/assets/46ad4cbc-3228-40de-a64e-2e0d9df248c4" />


### Software
- Arduino IDE
- Python
- PySerial
- Pandas
- Streamlit
- Matplotlib
- Scikit-learn
- Git & GitHub

### Hardware
- Arduino UNO Q
- ZMPT101B Voltage Sensor
- WCS1700 Hall Effect Current Sensor
- DS18B20 Temperature Probe
- MPU6050 Accelerometer & Gyroscope (Vibration Sensor)
- 180 W Single Phase Induction Motor

### Machine Learning
- Decision Tree
- Random Forest

### Features
- Real-time sensor acquisition
- Edge AI based health prediction
- Prediction confidence estimation
- Automatic CSV data logging
- Historical trend visualization
- Rule-based Health Score generation
- Maintenance recommendation engine
- Automatic Email Alert System

### Latest Progress
- Integrated ZMPT101B, WCS1700, DS18B20 and MPU6050 with Arduino UNO Q.
- Developed a complete Edge AI inference pipeline using Random Forest.
- Collected and labelled real-world sensor data under Healthy, Warning and Faulty operating conditions.
- Implemented Arduino Router Bridge communication between the microcontroller and Linux-based Python runtime.
- Developed a Streamlit dashboard for real-time monitoring, historical analysis and maintenance recommendations.
- Implemented automatic email notifications for newly detected faulty conditions.

## Project Status
Prototype Completed

The core hardware integration, Edge AI deployment, analytics dashboard and automated alert system have been successfully implemented. Future work includes cloud database integration, remote dashboard access, multi-machine monitoring and Remaining Useful Life (RUL) prediction.
