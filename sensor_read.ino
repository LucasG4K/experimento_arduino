#include <DallasTemperature.h>
#include <OneWire.h>

#define pinVoltage A0
#define ONE_WIRE_BUS 7

OneWire ourWire(ONE_WIRE_BUS);
DallasTemperature sensor(&ourWire);

void setup() {
  Serial.begin(9600);
  pinMode(pinVoltage, INPUT);
  sensor.begin();
}

float voltage;

void loop() {
  sensor.requestTemperatures();
  float leitura = sensor.getTempCByIndex(0);

  unsigned short reading_voltage = (analogRead(pinVoltage));
  voltage = reading_voltage * 5 / 1024.0 * 5;
    
  Serial.print(leitura);
  Serial.print(',');
  Serial.println(voltage);

  delay(100);
}
