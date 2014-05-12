from turtle import *

def square(color):
    fillcolor(color)
    begin_fill()
    fd(100)
    rt(90)
    fd(100)
    rt(90)
    fd(100)
    rt(180)
    end_fill()

def draw_panel():
    setworldcoordinates(0, 0, 300, 300)
    speed(0)
    penup()
    goto(100, 300)
    square('red')
    square('yellow')
    square('green')

# step 2: type code FROM this line
def switch(x, y):
    print('click at y = ', y)
    if 0 <= y < 100:
        bgcolor('dark green')
    elif 100 <= y < 200:
        bgcolor('#880')
    else:
        bgcolor('dark red')

onscreenclick(switch)
# step 2: type code TO this line

draw_panel()

mainloop()
