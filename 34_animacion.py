import turtle
t = turtle.Turtle()
t.speed(2)
angulo = 0
while True:
    t.clear()
    t.left(angulo)
    # t.forward(10)
    angulo += 1
    if angulo > 120:
        break
turtle.done()