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

//Sensor value list
int sensorValue[3] = {0,0,0};

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

  //int dF = distFront();
  //int dR = distRight();
  //int dL = distLeft();
  
  //read sensor values
  readSensors();
  
  //BTdevice.write("BTDEVICE");

  //send sensor values (list) to Rasp
  for(int k=0; k<3; k++)
  {
    Serial.print(sensorValue[k]);
    if(k<2){
      Serial.print(',');
    }

  }
  Serial.println();
  delay(2000);

  //recieve message from Rasp (ATM if msg = 1 move forward
  if (BTdevice.available() > 0){
    int msg = BTdevice.read();
    //Serial.println(msg);
    if(msg == 49)
    {
      forward();
      delay(1000);
      stopMotors();
    }
    if(msg == 48)
    {
      backward();
      delay(1000);
      stopMotors();
    }
    if(msg == 50)
    {
      right();
      delay(400);
      forward();
      delay(200);
      stopMotors();
    }
    if(msg == 51)
    {
      left();
      delay(400);
      forward();
      delay(200);
      stopMotors();
    }
  }
  
}

//SONAR SENSORS

void readSensors()
{
  sensorValue[0] = distFront();
  sensorValue[1] = distLeft();
  sensorValue[2] = distRight();
}

int distFront()
{
  int dF = sonar_front.ping_cm();
  return dF;
}

int distRight()
{
  int dR = sonar_right.ping_cm();
  return dR;
}

int distLeft()
{
  int dL = sonar_left.ping_cm();
  return dL;
}

//MOVEMENT OPTIONS
//Default speed 150, MAX = 255
void forward()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(BACKWARD);
  leftMotor2 -> run(BACKWARD);
}

void backward()
{
  rightMotor1 -> setSpeed(150);
  leftMotor2 -> setSpeed(150);
  rightMotor1 -> run(FORWARD);
  leftMotor2 -> run(FORWARD);
}

void left()
{
  rightMotor1 -> setSpeed(80);
  leftMotor2 -> setSpeed(80);
  rightMotor1 -> run(BACKWARD);
  leftMotor2 -> run(FORWARD);
}

void right()
{
  rightMotor1 -> setSpeed(80);
  leftMotor2 -> setSpeed(80);
  rightMotor1 -> run(FORWARD);
  leftMotor2 -> run(BACKWARD);
}

void stopMotors()
{
  rightMotor1 -> setSpeed(0);
  leftMotor2 -> setSpeed(0);
  rightMotor1 -> run(BRAKE);
  leftMotor2 -> run(BRAKE);
}
