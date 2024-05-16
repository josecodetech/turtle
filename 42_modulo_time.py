import turtle
import time
t = turtle.Turtle()
t.speed(2)
def dibujar_cuadrado(tamaño):
    for _ in range(4):
        t.forward(tamaño)
        t.right(90)
for tamaño in range(20, 101, 10):
    dibujar_cuadrado(tamaño)
    time.sleep(1)
turtle.done()