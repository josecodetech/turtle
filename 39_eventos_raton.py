import turtle
t = turtle.Turtle()
t.speed(2)
def mover(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
turtle.onscreenclick(mover)
turtle.done()