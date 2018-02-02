#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myMotor1 = AFMS.getMotor(1);
Adafruit_DCMotor *myMotor2 = AFMS.getMotor(2);

void setup()
{
  AFMS.begin();
  Serial.begin(9600);
  Serial.write('1');
}

void loop() 
{
  if (Serial.available() > 0)
  {
    myMotor1 ->setSpeed(150);
    myMotor2 ->setSpeed(150);
    myMotor1 ->run(FORWARD);
    myMotor2 ->run(FORWARD);
  }
}

