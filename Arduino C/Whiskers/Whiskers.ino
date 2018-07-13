#include <Servo.h> 

Servo servoLeft;    // Declare left servo signal
Servo servoRight;  //Declare right servo signal

void backwards() {
  servoLeft.writeMicroseconds(1700);       
  servoRight.writeMicroseconds(1300);
  }
void forwards(){
  servoLeft.writeMicroseconds(1300);       
  servoRight.writeMicroseconds(1700);
}
void turnL() {
   servoLeft.writeMicroseconds(1570);       
  servoRight.writeMicroseconds(1517);
}
void turnR() {
  servoLeft.writeMicroseconds(1517);       
  servoRight.writeMicroseconds(1570);
}
int whiskerLeft = 5;
int whiskerRight = 7;  

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);
 servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500); 
pinMode(whiskerLeft, INPUT );
pinMode(whiskerRight, INPUT);  
}


 
void loop() {
  // put your main code here, to run repeatedly:
  // Read the inputs from the whiskers and store them as a number
int leftValue = digitalRead(whiskerLeft); 
int rightValue = digitalRead(whiskerRight); 

  //Print
/*  Serial.print("Right: ");
  Serial.println(rightValue);
  Serial.print(" Left: ");
  Serial.print(leftValue);
  Serial.println("");
 delay(1000); 
 */
backwards();
if(leftValue == 1 && rightValue == 1){
  Serial.println("Go backwards! ");
  forwards();
  }
 else if (leftValue == 1){
  Serial.println("Turn right! ");
  turnR();
 }
 else if (rightValue == 1){
  Serial.println("Turn left! ");
  turnL();
 }
 else{
 backwards();
 }


//delay(100);
}
