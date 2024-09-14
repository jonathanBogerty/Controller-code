#define VRX_PIN  A0
#define VRY_PIN  A1
int xValue = 0;
int yValue = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  
}

void loop()

{   
  if(digitalRead(2) == HIGH){

  	Serial.println("Button");

  } else {

   	Serial.println("");
  }

  xValue = analogRead(VRX_PIN);
  yValue = analogRead(VRY_PIN);


  Serial.print("x = ");
  Serial.print(xValue);
  Serial.print(", y = ");
  Serial.println(yValue);
  delay(200);

}