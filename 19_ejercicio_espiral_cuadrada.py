import turtle
t = turtle.Turtle()
t.speed(4)
longitud = 15
for _ in range(20):
    t.forward(longitud)
    t.left(90)
    longitud += 10
turtle.done()
