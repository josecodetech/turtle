import turtle
t = turtle.Turtle()
t.speed(3)
t.penup()
x = -200
t.goto(x,0)
t.pendown()
while x < 200:
    t.goto(x, 0)
    x += 2
turtle.done()