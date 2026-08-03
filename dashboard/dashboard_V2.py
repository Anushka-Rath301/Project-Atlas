import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

tab1,tab2,tab3=st.tabs(["Overview","Analytics","AI Insights"])
df=pd.read_csv("D:/Anushka Projects/pandas/sensor_log.csv")


with tab1:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Overview:")
    with st.container(border=True):
        if df.iloc[:,5].mean()>80:
            st.write("Health Score:95/100")
            st.write("Healthy")
            st.write("Current:",round(df.iloc[:,1].mean()),"A")
            st.write("Voltage:",round(df.iloc[:,4].mean()),"V")
            st.write("Temperature:",round(df.iloc[:,3].mean()),"(C)")
            st.write("Vibration:",round(df.iloc[:,2].mean()),"g")
        elif df.iloc[:,5].mean()>50:
            st.write("Health Score:75/100")
            st.write("Warning")
            st.write("Current:",round(df.iloc[:,1].mean()),"A")
            st.write("Voltage:",round(df.iloc[:,4].mean()),"V")
            st.write("Temperature:",round(df.iloc[:,3].mean()),"(C)")
            st.write("Vibration:",round(df.iloc[:,2].mean()),"g")
        else:
            st.write("Health Score:40/100")
            st.write("Faulty")
            st.write("Current:",round(df.iloc[:,1].mean()),"A")
            st.write("Voltage:",round(df.iloc[:,4].mean()),"V")
            st.write("Temperature:",round(df.iloc[:,3].mean()),"(C)")
            st.write("Vibration:",round(df.iloc[:,2].mean()),"g")

with tab2:
    st.title("THE ANALYTICS DASHBOARD")
    st.header("Analytics:")
    col1,col2=st.columns(2)
    with col1:
        fig,ax=plt.subplots()
        recent = df.tail(20)
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature")
        ax.plot(recent["Time"], recent["Temperature"])
        st.pyplot(fig)

        fig2,axx=plt.subplots()
        recent = df.tail(20)
        axx.set_xlabel("Time")
        axx.set_ylabel("Vibration")
        axx.plot(recent["Time"], recent["Vibration"])
        st.pyplot(fig2)

    with col2:
        fig3,ay=plt.subplots()
        ay.set_xlabel("Time")
        ay.set_ylabel("Current")
        ay.plot(recent["Time"], recent["Current"])
        st.pyplot(fig3)

        fig4,ayy=plt.subplots()
        ayy.set_xlabel("Time")
        ayy.set_ylabel("Voltage")
        ayy.plot(recent["Time"], recent["Voltage"])
        st.pyplot(fig4)

with tab3:
    st.title("THE ANALYTICS DASHBOARD")
    with st.expander("Predictions"):
        st.write("Motor Health: Warning")
    with st.expander("Confidence"):
        st.write("92.4%")
    with st.expander("Fault Records"):
        st.write("Total Faults : 3,Last Fault :18 Jul 2026")
    with st.expander("Recommendation"):
        st.write("• Inspect motor bearings.")
        st.write("• Check shaft alignment.")
        st.write("• Monitor vibration over the next 24 hours.")
time.sleep(20)
st.rerun()

            
