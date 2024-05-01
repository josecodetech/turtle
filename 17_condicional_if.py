import turtle
t = turtle.Turtle()

lados = 14
if lados % 2 == 0:
    for _ in range(4):
        t.forward(100)
        # t.left(360/lados)
        t.left(90)
else:
    for _ in range(3):
        t.forward(100)
        t.left(120)
turtle.done()