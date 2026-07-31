#include "WCS1700.h" // current sensor lib
#include <Wire.h>      // I2C communication lib
#include <MPU6050.h>   // MPU lib
#include <OneWire.h>   // OneWire Communication Lib
#include <DallasTemperature.h> // temperature sensor lib
#include <Arduino_RouterBridge.h> // bridge between MCU and MPU communication 

#define VOLTAGE_PIN A0
const float VREF = 3.3;
const float ADC_MAX = 1023.0;
const float SENSITIVITY = 577.5;

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
Serial.begin(115200);
Wire.begin();
Bridge.begin();
mpu.initialize();
sensors.begin();
analogReadResolution(10);

  // Power-on Reset
  WCS1.Reset();
}

void loop() {
//Voltage Readings
int raw = analogRead(VOLTAGE_PIN);
float voltage = (raw * VREF / ADC_MAX) * SENSITIVITY;

// Hardware calibration factor determined experimentally
// using reference mains voltage measurements.
// Adjust if the sensor or calibration setup changes.
voltage = voltage * 0.174;
Serial.print(raw);
if (voltage < 5) {
    voltage = 0;
}

//Current Readings
float current = WCS1.A_AC();
if (current<0.3){
  current=0;
}

//Vibration Readings
mpu.getAcceleration(&ax,&ay,&az);
float ax_g = ax / 16384.0;
float ay_g = ay / 16384.0;
float az_g = az / 16384.0;
float vibration =sqrt(ax_g*ax_g +ay_g*ay_g +az_g*az_g);

//Temperature Readings
sensors.requestTemperatures();

float tempC = sensors.getTempCByIndex(0);
  if (tempC == DEVICE_DISCONNECTED_C)
  {
    tempC=-999; // Error Value
  }
Serial.print(",");
Serial.print(voltage);
Serial.print(",");
Serial.print(current);
Serial.print(",");
Serial.print(vibration);
Serial.print(",");
Serial.println(tempC);

auto response=Bridge.call("rec_values",voltage,current,vibration,tempC);

delay(750);
}




