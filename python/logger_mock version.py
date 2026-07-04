import serial 
import csv
from datetime import datetime 

#let the rated current of motor-10A
hscore=100 #health score variable 
hstatus=''

ard_data=serial.Serial("COM3",115200)  #python object to receive values 

#writing the data into csv files
with open("D:/Anushka Projects/pandas/sensor_log.csv",mode="w") as file:
    w=csv.writer(file)
    w.writerow(["Time","Current","Vibration","Temperature","Voltage","Health Score","Health Status"])
    while True:
        dp=ard_data.readline().decode("UTF-8").strip("\r\n")
        dp=dp.split(',') 
        time=datetime.now().strftime("%H:%M:%S")
        dp.insert(0,time)  #[time,curr,vib,temp,volt]
        dp[1]=float(dp[1])
        dp[2]=float(dp[2])
        dp[3]=float(dp[3])
        dp[4]=float(dp[4])
        
        if (dp[3]<40) and (220<dp[4]<=240) and (9.5<dp[1]<10.5) and dp[2]<0.3:
            hscore=100
            hstatus="HEALTHY"
            dp.append(hscore)
            dp.append(hstatus)
        elif (40<dp[3]<=55) and (210<dp[4]<220) or (240<dp[4]<250) and (10<dp[1]<12) and (0.3<dp[2]<0.6):
            hscore=100-10-15-8-18
            hstatus="WARNING"
            dp.append(hscore)
            dp.append(hstatus)
        elif (dp[3]>55) and (dp[4]<210) or (dp[4]>250) and (dp[1]>12) and (dp[2]>0.6):
            hscore=100-20-15-35-30
            hstatus="FAULTY"
            dp.append(hscore)
            dp.append(hstatus)
        else:
            hscore = 75
            hstatus = "WARNING"
            dp.append(hscore)
            dp.append(hstatus)
        w.writerow(dp)
        print(dp)
        file.flush()
        

        