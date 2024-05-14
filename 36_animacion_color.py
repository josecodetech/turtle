import turtle
t = turtle.Turtle()
t.speed(1)
colores = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
indice = 0

# while True:
for color in colores:
    t.color(color)
    t.forward(120)
    t.left(90)
    # indice = (indice + 1) % len(colores)
turtle.done()