

String s1;
void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);

void loop() {
  if(Serial.available())                 
{ s1=Serial.readStringUntil('\n');
  Serial.println(s1);
  
  int data =s1.toInt();
  //Serial.println("data is");
  //Serial.println(data);
  if (data==1)
  {
    analogWrite(5,255);
    analogWrite(6,0);
    analogWrite(9,255);
    analogWrite(10,0); 
  }
  else if (data==5)
  {
    analogWrite(5,255);
    analogWrite(6,0);
    analogWrite(9,255);
    analogWrite(10,0); 
  }
  else if (data==3)
  {
    analogWrite(5,153);
    analogWrite(6,0);
    analogWrite(9,0);
    analogWrite(10,0);  
  }
  else if (data==4)
  {
    analogWrite(5,204);
    analogWrite(6,0);
    analogWrite(9,0);
    analogWrite(10,0);  
  }
  else if (data==5)
  {
    analogWrite(5,255);
    analogWrite(6,0);
    analogWrite(9,0);
    analogWrite(10,0);  
  }
  else if (data==6)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,51);
    analogWrite(10,0);  
  }
  else if (data==7)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,102);
    analogWrite(10,0);  
  }
  else if (data==8)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,153);
    analogWrite(10,0);  
  }
  else if (data==9)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,204);
    analogWrite(10,0);  
  }
  else if (data==10)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,255);
    analogWrite(10,0);  
  }
    else if (data==11)
  {
    analogWrite(5,51);
    analogWrite(6,0);
    analogWrite(9,51);
    analogWrite(10,0);  
  }
  else if (data==12)
  {
    analogWrite(5,102);
    analogWrite(6,0);
    analogWrite(9,102);
    analogWrite(10,0);  
  }
  else if (data==13)
  {
    analogWrite(5,153);
    analogWrite(6,0);
    analogWrite(9,153);
    analogWrite(10,0);  
  }
  else if (data==14)
  {
    analogWrite(5,204);
    analogWrite(6,0);
    analogWrite(9,204);
    analogWrite(10,0);  
  }
  else if (data==15)
  {
    analogWrite(5,255);
    analogWrite(6,0);
    analogWrite(9,255);
    analogWrite(10,0);  
  }
  else if (data==16)
  {
    analogWrite(5,0);
    analogWrite(6,51);
    analogWrite(9,0);
    analogWrite(10,51);  
  }
  else if (data==17)
  {
    analogWrite(5,0);
    analogWrite(6,102);
    analogWrite(9,0);
    analogWrite(10,102);  
  }
  else if (data==18)
  {
    analogWrite(5,0);
    analogWrite(6,153);
    analogWrite(9,0);
    analogWrite(10,153);  
  }
  else if (data==19)
  {
    analogWrite(5,0);
    analogWrite(6,204);
    analogWrite(9,0);
    analogWrite(10,204);  
  }
  else if (data==20)
  {
    analogWrite(5,0);
    analogWrite(6,255);
    analogWrite(9,0);
    analogWrite(10,255);  
  }
    else if (data==21)
  {
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(9,0);
    analogWrite(10,0);  
  }  
}
}
