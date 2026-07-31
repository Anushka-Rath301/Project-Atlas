import subprocess
import time

while True:
    subprocess.run(["C:/Users/ajayn/Downloads/platform-tools-latest-windows/platform-tools/adb.exe","pull","/home/arduino/ArduinoApps/atlas/python/sensor_log.csv",r"D:\Anushka Projects\deploy\python\sensor_log.csv"])
    time.sleep(2)