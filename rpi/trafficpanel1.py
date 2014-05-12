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


draw_panel()

mainloop()
