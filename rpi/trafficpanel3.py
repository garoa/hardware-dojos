from turtle import *
from trafficleds import activate

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

def switch(x, y):
    print('click at y = ', y)
    if 0 <= y < 100:
        bgcolor('dark green')
        activate('green')
    elif 100 <= y < 200:
        bgcolor('#880')
        activate('yellow')
    else:
        bgcolor('dark red')
        activate('red')

draw_panel()

onscreenclick(switch)

mainloop()
