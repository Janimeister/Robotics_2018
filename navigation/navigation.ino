#include <Wire.h>
#include <NewPing.h> //https://bitbucket.org/teckel12/arduino-new-ping/downloads/ NEEDED FOR UltraSonic sensors
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

//LEFT
#define LFT_TRIGGER_PIN 2
#define LFT_ECHO_PIN 3
//FRONT
#define FRNT_TRIGGER_PIN 4
#define FRNT_ECHO_PIN 5
//RIGHT
#define RGHT_TRIGGER_PIN 6
#define RGHT_ECHO_PIN 7

#define MAX_DISTANCE 600 //MAX DISTANCE FOR THE SENSORS

NewPing sonar_left(LFT_TRIGGER_PIN, LFT_ECHO_PIN, MAX_DISTANCE);
NewPing sonar_front(FRNT_TRIGGER_PIN, FRNT_ECHO_PIN, MAX_DISTANCE);
NewPing sonar_right(RGHT_TRIGGER_PIN, RGHT_ECHO_PIN, MAX_DISTANCE);


Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *rightMotor1 = AFMS.getMotor(1);
Adafruit_DCMotor *leftMotor2 = AFMS.getMotor(2);

void setup()
{
  AFMS.begin();
  Serial.begin(9600);
}

void loop()
{
  int luku = sonar_right.ping_cm();
  /*
  if (Serial.available() > 0)
  {
    if (Serial.read() == '1')
    {
        rightMotor1 ->setSpeed(150);
        leftMotor2 ->setSpeed(150);
        rightMotor1 ->run(FORWARD);
        leftMotor2 ->run(FORWARD);
    }
    if (Serial.read() == '0')
    {
        rightMotor1 ->setSpeed(0);
        leftMotor2 ->setSpeed(0);
        rightMotor1 ->run(BRAKE);
        leftMotor2 ->run(BRAKE);
    }
  }
  */
  
}

//MOVEMENT OPTIONS
//Default speed 150, MAX = 255
void forward()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(FORWARD);
  leftMotor2 -> run(FORWARD);
}

void backward()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(BACKWARD);
  leftMotor2 -> run(BACKWARD);
}

void left()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(FORWARD);
  leftMotor2 -> run(BACKWARD);
}

void right()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(BACKWARD);
  leftMotor2 -> run(FORWARD);
}

void stop()
{
  rightMotor1 -> setSpeed(0);
  leftMotor2 -> setSpeed(0);
  rightMotor1 -> run(BRAKE);
  leftMotor2 -> run(BRAKE);
}



