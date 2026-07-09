# Project Atlas

## Edge AI-based Predictive Maintenance and Health Monitoring System for Small Electrical Machines

Project Atlas is an Edge AI solution designed to monitor the health of small electrical machines in real time using the Arduino UNO Q.

The system acquires sensor data such as current, voltage, temperature, and vibration, performs on-device AI inference to predict machine health, logs operational data, and visualizes historical trends through an analytics dashboard.

## Objectives

* Real-time health monitoring
* Predictive maintenance using Edge AI
* Local AI inference on Arduino UNO Q
* Cloud connectivity via Wi-Fi/MQTT
* Interactive analytics dashboard
* Maintenance recommendations based on historical trends

## System Architecture

![System Architecture](docs/architecture_v1.png)

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
- MySQL *(In Progress)*
- Git & GitHub

### Machine Learning
- Decision Tree
- Random Forest

### Alerts
- SMTP Email Notifications
- SMS Alerts *(Planned)*

### Latest Progress
- Integrated Voltage (ZMPT101B), Current (WCS1700), Temperature (DS18B20) and Vibration (MPU6050) sensors.
- Implemented real-time sensor acquisition using Arduino UNO Q.
- Developed Python script for serial communication and automatic CSV dataset generation.
- Collected real-world vibration data under multiple operating conditions for AI model training.

## Project Status

🚧 Currently under development.

This repository will be updated as the project progresses.
