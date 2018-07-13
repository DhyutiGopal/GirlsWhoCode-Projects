void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT); //13 -> The number pin where the power is coming from

  

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH); //turn on LED by making voltage High level
  delay(500); //wait for a second
  digitalWrite(13, LOW); //turn off the LED by making voltage low
  delay(500); //wait for a second
}
