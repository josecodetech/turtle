import turtle
t = turtle.Turtle()
t.speed(9)
t.width(1)
angulo = 91
while angulo > 1:
    t.forward(5)
    t.right(angulo)
    angulo -= 0.1 # angulo = angulo - 0.1
turtle.done()
   