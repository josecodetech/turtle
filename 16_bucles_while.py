import turtle

t = turtle.Turtle()
lados = 0
while lados < 5:
    t.forward(100)
    t.left(360/5)
    lados += 1  
turtle.done()