#include <Servo.h>
#include <math.h>
#include <SoftwareSerial.h>
#include <TFMini.h>

int minAngle = 0;   // gripper fully open
int maxAngle = 50;  // gripper fully closed

SoftwareSerial mySerial(10, 11);
TFMini tfmini;
Servo myservo;
String msg;
uint16_t dist;

void setup() {
  Serial.begin(9600);  // initialize serial communication at 9600 baud
}

void loop() {
  if (Serial.available()) {  // check if there's data in the serial buffer
    String inputString = "";  // create an empty string to hold the incoming data
    while (Serial.available()) {
      char incomingChar = Serial.read();  // read the incoming character
      inputString += incomingChar;  // append the character to the input string
      delay(5);  // wait a short time for the next character
    }
    String command = inputString;
    Serial.println("Received: " + command);  // print the received string to the serial monitor
    command.trim();         // get rid of extra spaces or CR/LF if there's any
    command.toLowerCase();  // always convert to lowercase (case insensitive)
    Serial.println(command);
    if (command == "lidar" || command == "l") {
      for (int x = 0; x < 5; x++) { // make 5x reading for reliability
        dist = tfmini.getDistance();
        delay(50);
      }
      msg = "LIDAR distance in cm = " + String(dist);
    }
    if (command == "gripper 0" || command == "g0") {  // fully open
      myservo.write(0);
      msg = "Gripper 0 fully opened";
    }
        if (command == "gripper 20" || command == "g20") {
      myservo.write(20);
      msg = "Gripper 20";
    }
    if (command == "gripper 30" || command == "g30") {
      myservo.write(30);
      msg = "Gripper 30";
    }
    if (command == "gripper 40" || command == "g40") {
      myservo.write(40);
      msg = "Gripper 40";
    }
    if (command == "gripper 50" || command == "g50") {  // fully closed
      myservo.write(50);
      msg = "Gripper 50 fully closed";
    }
    Serial.println(msg);
    Serial.println("OK");
  }
}
