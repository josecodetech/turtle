import turtle
import random
t = turtle.Turtle()
t.speed(2)
def dibujar_cuadrado():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    tamaño = random.randint(20,100)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for _ in range(4):
        t.forward(tamaño)
        t.right(90)
for _ in range(10):
    dibujar_cuadrado()
turtle.done()