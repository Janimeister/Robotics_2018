#include <Wire.h>
#include <NewPing.h> //https://bitbucket.org/teckel12/arduino-new-ping/downloads/ NEEDED FOR UltraSonic sensors
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <SoftwareSerial.h>

//LEFT
#define LFT_TRIGGER_PIN 2
#define LFT_ECHO_PIN 3
//FRONT
#define FRNT_TRIGGER_PIN 4
#define FRNT_ECHO_PIN 5
//RIGHT
#define RGHT_TRIGGER_PIN 6
#define RGHT_ECHO_PIN 7

#define MAX_DISTANCE 200 //MAX DISTANCE FOR THE SENSORS

SoftwareSerial BTdevice(0,1);
String string;
char command;

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
  BTdevice.begin(9600);
}

void loop()
{
  if (BTdevice.available() > 0){
    int test = BTdevice.read();
    Serial.println(test);
  }
  delay(1000);
  int luku = sonar_front.ping_cm();
  int luku2 = sonar_left.ping_cm();
  int luku3 = sonar_right.ping_cm();
  //Serial.println("Front_sensor: Cm");
  //Serial.print(luku);
  //Serial.println("left_sensor: Cm");
  //Serial.print(luku2);
  //Serial.println("right_sensor: Cm");
  //Serial.print(luku3);
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



