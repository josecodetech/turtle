import random
import turtle
turtle.register_shape("flower",((0,0),(0,20),(10,30),(0,40),(-10,30),(0,20)))
t = turtle.Turtle()
t.speed(4)
turtle.bgcolor("lightgreen")
def dibujar_flor(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.shape("flower")
    t.stamp()
    
for _ in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    dibujar_flor(x,y)
turtle.done()
