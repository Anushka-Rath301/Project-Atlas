#include <WinsonLib.h>
#include <ZMPT101B.h>

ZMPT101B Voltage_sensor(A0,50);
WCS  WCS1 = WCS( 1, _WCS1700);

double data = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
Voltage_sensor.setSensitivity(577.5);
  // Power-on Reset
  Serial.println("Reset");
  WCS1.Reset();

}
void loop() {
  // put your main code here, to run repeatedly:
float voltage=Voltage_sensor.getRmsVoltage();
Serial.print("voltage :");
if(voltage<5){
  voltage=0;
  
  Serial.println(voltage);
}
else{
  Serial.println(voltage);
}

delay(500);
data = WCS1.A_AC();
  Serial.print("Current(A) : ");

  Serial.println(String(abs(data-.155)) + " A");
  
delay(500);
}




