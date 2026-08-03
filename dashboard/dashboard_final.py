import streamlit as st
import pandas as pd
import time
import joblib
model = joblib.load("motor_health_model.pkl")
import matplotlib.pyplot as plt

tab1,tab2,tab3=st.tabs(["Overview","Analytics","AI Insights"])
df=pd.read_csv("D:/Anushka Projects/deploy/python/sensor_log.csv")


recent = df.tail(20)
features=[[recent["Voltage"].mean(),recent["Current"].mean(),recent["Vibration"].mean(),recent["Temperature"].mean()]]

warning_count = (recent["Health Status"] == "Warning").sum()
fault_count = (recent["Health Status"] == "Faulty").sum()

if fault_count > 1:
    prediction = "Faulty"
elif warning_count > 3:
    prediction = "Warning"
else:
    prediction = "Healthy"


if prediction == "Warning":
    score = 75
else:
    score = 30

confidence = round(recent["Confidence"].mean(), 2)

classes=model.classes_  #we get the order in which healthy,faulty and warning are arranged
index=list(classes).index(prediction) #we get the index of corresponding health status

recommendation=''
if recent["Voltage"].mean()<210 or recent["Voltage"].mean()>250:
    recommendation+="Unstable voltage supply\n"
if recent["Current"].mean()>8:
    recommendation+="Overheating\n"
    recommendation+="overloading suspected\n"
    recommendation+="try to monitor the temperature and minimise the load\n"
if recent["Vibration"].mean()>1.5:                      
    recommendation+="Possible rotor imbalance detected\n"
    recommendation+="Inspect bearings and shaft alignment\n"
    recommendation+="Continue monitoring vibration trend\n"
    recommendation+="Check mounting bolts\n"
if recent["Vibration"].mean()>=1:
    recommendation+="Vibration Detected"  
if recent["Temperature"].mean()>55:
    recommendation+="Overheating detected, turn on the coolant\n"
if recommendation=='':
    recommendation+="motor is working fine\n"

score=100

if recent["Voltage"].mean() < 210 or recent["Voltage"].mean() > 250:
    score -= 10

if recent["Current"].mean() > 8:
    score -= 25

if recent["Temperature"].mean() > 55:
    score -= 20

if recent["Vibration"].mean() > 1.5:
    score -= 35

score = max(score,0) #to ensure positive number

with tab1:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Overview:")
    with st.container(border=True):
        if score>65:
            st.write("Health Score:",score)
            st.metric("Health Status",prediction)
            st.write("Current:",round(recent["Current"].mean()),"A")
            st.write("Voltage:",round(recent["Voltage"].mean()),"V")
            st.write("Temperature:",round(recent["Temperature"].mean()),"(C)")
            st.write("Vibration:",round(recent["Vibration"].mean()),"g")
        elif score>35:
            st.write("Health Score:",score)
            st.metric("Health Status",prediction)
            st.write("Current:",round(recent["Current"].mean()),"A")
            st.write("Voltage:",round(recent["Voltage"].mean()),"V")
            st.write("Temperature:",round(recent["Temperature"].mean()),"(C)")
            st.write("Vibration:",round(recent["Vibration"].mean()),"g")
        else:
            st.write("Health Score:",score)
            st.metric("Health Status",prediction)
            st.write("Current:",round(recent["Current"].mean()),"A")
            st.write("Voltage:",round(recent["Voltage"].mean()),"V")
            st.write("Temperature:",round(recent["Temperature"].mean()),"(C)")
            st.write("Vibration:",round(recent["Vibration"].mean()),"g")

with tab2:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Analytics:")
    col1,col2=st.columns(2)
    with col1:
        fig,ax=plt.subplots()
        ax.set_xlabel("Sample Number")
        ax.set_ylabel("Temperature")
        ax.plot(recent.index, recent["Temperature"])
        st.pyplot(fig)

        fig2,axx=plt.subplots()
        axx.set_xlabel("Sample Number")
        axx.set_ylabel("Vibration")
        axx.plot(recent.index, recent["Vibration"])
        st.pyplot(fig2)

    with col2:
        fig3,ay=plt.subplots()
        ay.set_xlabel("Sample Number")
        ay.set_ylabel("Current")
        ay.plot(recent.index, recent["Current"])
        st.pyplot(fig3)

        fig4,ayy=plt.subplots()
        ayy.set_xlabel("Sample Number")
        ayy.set_ylabel("Voltage")
        ayy.plot(recent.index, recent["Voltage"])
        st.pyplot(fig4)

with tab3:
    st.title("THE ANALYTICS DASHBOARD")

    with st.expander("Predictions"):
        if prediction=="Healthy":
            st.write("Motor Health:",prediction)
            st.success("Motor is healthy")
        elif prediction=="Warning":
            st.write("Motor Health:",prediction)
            st.warning("Motor needs inspection")
        else:
            st.write("Motor Health:",prediction)
            st.error("Fault Detected")

    with st.expander("Confidence"):
        st.write(confidence)

    with st.expander("Fault Records"):
        fc = (recent["Health Status"] == "Faulty").sum()
        st.write("total faults in the last 20 readings=",fc,"last reading:",recent.iloc[-1]["Time"])
        
    with st.expander("Recommendation"):
        st.text(recommendation)

from email_setup_mock import send_email

if prediction=="Faulty" and recent.iloc[-2]["Health Status"]!="Faulty":
    receiver_mail="anushkamusic25@gmail.com"
    Subject="Faulty Condition Detected"
    body=recommendation
    send_email(receiver_mail,Subject,body)
time.sleep(50)
st.rerun()

            
