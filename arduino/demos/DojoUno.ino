/*
  DojoUNO

  This example code is in the public domain.
 */


//                A   B  C  D  E  F   G
int display[] = {12, 13, 7, 8, 9, 11, 10};
const int SEGMENTS = 6;

void setup() {
  for (int i=0; i<SEGMENTS; i++) {
    pinMode(display[i], OUTPUT);
  }
}

void loop() {
  for (int i=0; i<SEGMENTS; i++) {
    digitalWrite(display[i], HIGH);
    delay(analogRead(A0));              
    digitalWrite(display[i], LOW);   
  }
}
