#include "WCS1700.h" // current sensor lib
#include <Wire.h>      // I2C communication lib
#include <MPU6050.h>   // MPU lib
#include <ZMPT101B.h>  // Voltage sensor lib 
#include <OneWire.h>   // OneWire Communication Lib
#include <DallasTemperature.h> // temperature sensor lib

ZMPT101B Voltage_sensor(A0,50); // ZMPT101B instance
WCS1700 WCS1(A1, _WCS1700);          // WCS instanace 
MPU6050 mpu;                   // MPU6050 Instance

#define ONE_WIRE_BUS 2
// a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

double data = 0;
int16_t ax,ay,az; // Acceleration variables 


void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
Wire.begin();
mpu.initialize();
sensors.begin();
analogReadResolution(10);
Voltage_sensor.setSensitivity(577.5);
  // Power-on Reset
  Serial.println("Reset the Current Sensor");
  WCS1.Reset();
}

void loop() {
  // put your main code here, to run repeatedly:
//Voltage Readings
float voltage=Voltage_sensor.getRmsVoltage();
v=voltage;
Serial.print("voltage :");
if(voltage<5){
  voltage=0;
  Serial.println(String(voltage) + "V");
}else{
  Serial.println(voltage);
}
delay(1000);

//Current Readings
data = WCS1.A_AC();
Serial.print("Current(A): ");
Serial.print(data, 3);
Serial.println(" A"); 
delay(1000);

//Vibration Readings
mpu.getAcceleration(&ax,&ay,&az);
Serial.print(ax);
Serial.print(",");
Serial.print(ay);
Serial.print(",");
Serial.println(az);
float ax_g = ax / 16384.0;
float ay_g = ay / 16384.0;
float az_g = az / 16384.0;
float vibration =
sqrt(
ax_g*ax_g +
ay_g*ay_g +
az_g*az_g
);
Serial.print("vibration");
Serial.println(vibration);
delay(1000);

//Temperature Readings
sensors.requestTemperatures();
delay(750);

float tempC = sensors.getTempCByIndex(0);
 // Error Handling
  if (tempC != DEVICE_DISCONNECTED_C)
  {
    Serial.print("Temperature  is: ");
    Serial.println(tempC);
  }
  else
  {
    Serial.println("Error: Could not read temperature data");
  }

}




