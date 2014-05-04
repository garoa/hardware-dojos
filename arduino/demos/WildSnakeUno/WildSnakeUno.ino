/*
  SnakeUNO

Snake head position and direction is coded like pictured below, i.e. when
the snake head is at the middle segment going right, the code is 6, going 
left in the same place is code 13.

       >:0
       <:7
      -----
^:5  |     | v:1
v:12 | >:6 | ^:8
      -----
^:4  | <:13| v:2
v:11 |     | ^:9
      -----
       <:3
       >:10

To understand this diagram, read:

> as a right arrow
< as a left arrow
v as a down arrow
^ as an up arrow

The moves array lists possible moves for each head position/direction.

*/

// {number_of_choices, first_choice, second_choice_if_available}
int moves[][3] = {
  {1, 1, -1},  // 0
  {2, 13, 2},  // 1
  {1, 3, -1},  // 2
  {1, 4, -1},  // 3
  {2, 6, 5},   // 4
  {1, 0, -1},  // 5
  {2, 2, 8},   // 6
  {1, 12, -1}, // 7
  {1, 7, -1},  // 8
  {2, 13, 8},  // 9
  {1, 9, -1},  // 10
  {1, 10, -1}, // 11
  {2, 6, 11},  // 12
  {2, 5, 11}   // 13
};

/*     A
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

int head = 1; // segment A
int tail = 0; // segment F

void setup() {
  for (int i=0; i<SEGMENTS; i++) {
    pinMode(display[i], OUTPUT);
  }
}

void loop() {
    digitalWrite(display[head % 7], HIGH);
    delay(analogRead(A0));
    digitalWrite(display[tail % 7], LOW);
    tail = head;
    int num_choices = moves[head][0];
    head = moves[head][random(num_choices)+1];
}
