/*
  DojoXXG_Snake

  This example code is in the public domain.
 */

const int FIRST_LED = 6;
const int LAST_LED = 12;
const int DOT_LED = 9;
const int DELAY = 100;

void setup() {
  for (int i=FIRST_LED; i<=LAST_LED; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  for (int i=FIRST_LED; i<=LAST_LED; i++) {
    if (i == DOT_LED) continue;
    digitalWrite(i, HIGH);
    delay(analogRead(A0));              
    digitalWrite(i, LOW);   
  }
}
