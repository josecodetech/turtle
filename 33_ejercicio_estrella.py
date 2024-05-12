import turtle
t = turtle.Turtle()
t.speed(5)
def estrella(tamaño):
    for _ in range(5):
        t.forward(tamaño)
        t.right(144)
for _ in range(20):
    estrella(50)
    t.right(18)
turtle.done()
