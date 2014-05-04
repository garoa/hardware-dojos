/*
  SnakeUNO

  This example code is in the public domain.
 */


//                A   B  C  D  E   F   G
int display[] = {12, 13, 7, 8, 9, 11, 10};
const int SEGMENTS = 7;

//             A   B   G  E  D  C   G   F
int path[] = {12, 13, 10, 9, 8, 7, 10, 11};
const int STEPS = 8;

int tail = path[STEPS-1];

void setup() {
  for (int i=0; i<SEGMENTS; i++) {
    pinMode(display[i], OUTPUT);
  }
}

void loop() {
  for (int i=0; i<STEPS; i++) {
    digitalWrite(path[i], HIGH);
    delay(analogRead(A0));              
    digitalWrite(tail, LOW);
    tail = path[i];   
  }
}
