#include "MeOrion.h"
#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Wire.h>

long vitesse = 100;

MeWifi Wifi(PORT_4);
unsigned long myTime;

MeDCMotor motor_9(9); //Motor1 on port 9
MeDCMotor motor_10(10); //Motor2 on port 10
MeDCMotor motor_1(1); // motor UpDown
MeDCMotor motor_2(2); // motor UpDown
char outChar;
char inCmd;

void setup() {
   Serial.begin(9600);
    Wifi.begin(9600);
    Serial.println("Wifi Start!");
}

void loop()
{ 
   if(Wifi.available())
    {
        Serial.println("Wifi on!");
        inCmd = read_wifi();        //Read Wifi input
        String msg; 
        switch(inCmd){                //Do what you've been told :-) 12 commandes possibles
        Serial.print("THATSSS A TESTTT : ");
        Serial.print(inCmd);
            case 'F': // forward
                  Serial.print(vitesse);
                  motor_9.run(-vitesse);
                  motor_10.run(vitesse);
                  break;
                
              case 'B': // Backward
                motor_9.run(vitesse);
                motor_10.run(-vitesse);
                break;
              case 'L': //Left
                motor_10.run(vitesse);
                // motor_9.run(0);
                motor_9.run(vitesse);
                break;
              case 'R': // Right
                motor_9.run(-vitesse);
                // motor_10.run(0);
                motor_10.run(-vitesse);
                break;
              case 'A': // Arret or Stop
                motor_10.run(0);
                motor_9.run(0);
            case 'u':  //head Up
                Serial.println(inCmd);
                motor_2.run(-100);
                break;
           
            case 'D': // head down
                motor_2.run(100);
                Serial.println(inCmd);
                break;
            case 'H': // Stop head motor
                motor_2.run(0);
                Serial.println(inCmd);
                break;
            case 'S': // Stop gripper
                motor_1.run(0);
                Serial.println(inCmd);
                break;
            case 'G': // grab
                motor_1.run(80);
                Serial.println(inCmd);
                break;
            case 'U': // ungrab
                motor_1.run(-80);
                Serial.println(inCmd);
                break;
            case 'v': // vitesse1
                // motor_1.run(-80);
                vitesse = 100;
                Serial.println(inCmd);
                break;
            case 'p': // vitesse2
                // motor_1.run(-80);
                vitesse = 200;
                Serial.println(inCmd);
                break;
            case 'k': // vitesse3
                // motor_1.run(-80);
                vitesse = 300;
                Serial.println(inCmd);
                break;
            // F
            case '0':
                Serial.println(inCmd);
                break;
            
            case 'c': //connection
                Serial.println("Client connected");
                Wifi.write(200);
                break;
            
            case 'd': //deconnection
                Serial.println("Client disconnected");
                Wifi.write('404');
                break;
            
            default:
                Serial.println("message non identifié");
                motor_1.run(0);
                motor_2.run(0);
                motor_9.run(0);
                motor_10.run(0);
                break;

          }  
    }
    
  
}

/*Wifi read function*/
char read_wifi(){
  char wfIn;
  wfIn = (char) Wifi.read();
  return wfIn;
}

void serialEvent() {
    Serial.println("envoi");
    if (Serial.available()) {
    // get the new byte:
    outChar = (char)Serial.read();
    Serial.println(outChar); //char to send
    Wifi.write(outChar);
  }
}
