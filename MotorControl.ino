int ledPin = 9;      // LED connected to digital pin 9
// int analogPin = 3;   // potentiometer connected to analog pin 3
int val = 0;         // variable to store the read value
const int analogInPin1 = A0; 
const int analogInPin2 = A1;
const int analogInPin3 = A3;
const int analogInPin4 = A4;
 
int sensorValue1 = 0;  
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int foo = 0;
int hello = 0;
 
void setup()
{
  pinMode(ledPin, OUTPUT);   // sets the pin as output
}
 
void loop()
{
  sensorValue1 = analogRead(analogInPin1);
  sensorValue2 = analogRead(analogInPin2);
  sensorValue3 = analogRead(analogInPin3); 
  sensorValue4 = analogRead(analogInPin4);  
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);           
 
  // print the results to the serial monitor:
  Serial.print("sensor1 = " );                       
  Serial.println(sensorValue1); 
  Serial.println(sensorValue2);  
  Serial.println(sensorValue3);
  Serial.println(sensorValue4);
  
  hello = sensorValue4;
  
  if (hello < 300)
      foo = 180;
         
      else
          foo = 255;
  
  //val = analogRead(analogPin);   // read the input pin
  analogWrite(ledPin, foo);  // analogRead values go from 0 to 1023, analogWrite values from 0 to 255
}  
