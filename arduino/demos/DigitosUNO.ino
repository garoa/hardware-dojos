/*
  DigitosUNO

       A
     -----
  F |     | B
    |  G  |
     -----
  E |     | C
    |  D  |
     ----- 
*/

//                A   B  C  D  E   F   G
int display[] = {12, 13, 7, 8, 9, 11, 10};
const int SEGMENTS = 7;

int digits[][SEGMENTS] = {
// A  B  C  D  E  F  G
  {1, 1, 1, 1, 1, 1, 0},  // 0
  {0, 1, 1, 0, 0, 0, 0},  // 1
  {1, 1, 0, 1, 1, 0, 1},  // 2
  {1, 1, 1, 1, 0, 0, 1},  // 3
  {0, 1, 1, 0, 0, 1, 1},  // 4
  {1, 0, 1, 1, 0, 1, 1},  // 5
  {1, 0, 1, 1, 1, 1, 1},  // 6
  {1, 1, 1, 0, 0, 0, 0},  // 7
  {1, 1, 1, 1, 1, 1, 1},  // 8
  {1, 1, 1, 1, 0, 1, 1}   // 9
};
const int DIGITS = 10;

void setup() {
  for (int i=0; i<SEGMENTS; i++) {
    pinMode(display[i], OUTPUT);
  }
}

void loop() {
  for (int digit=0; digit<DIGITS; digit++) {
    for (int segment=0; segment<SEGMENTS; segment++) {
      digitalWrite(display[segment], digits[digit][segment] == 1 ? HIGH : LOW);
    }
    delay(analogRead(A0));
  }
}
