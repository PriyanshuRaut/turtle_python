from turtle import *
import turtle as t

screen = t.Screen()
screen.setup(524, 512)

t.penup()
t.teleport(x = -256,y = -228)
t.pendown()
t.forward(498)
t.left(90)
t.forward(470)
t.left(90)
t.forward(498)
t.left(90)
t.forward(470)
t.left(90)
t.penup()

t.teleport(x=0,y=-100)
t.color("yellow")
t.begin_fill()
t.circle(140)
t.end_fill()

def draw_eye(x, y):
    
    t.teleport(x = x,y = y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()

    
    t.teleport(x = x,y = y + 5)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()

def draw_mouth(x,y):
    t.teleport(x = x,y = y)
    t.pendown()
    t.color("black")
    t.setheading(-60)
    t.circle(50, 120)
    t.penup()


draw_eye(-70, 60)
draw_eye(30, 60)
draw_mouth(-40, -30)

t.hideturtle()
t.mainloop()
