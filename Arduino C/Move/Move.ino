#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal


void setup()
{                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
  // Attach LED pins here.
  
}  
 
void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  servoLeft.writeMicroseconds(1520);        
  servoRight.writeMicroseconds(1518);
  delay(500);
}


