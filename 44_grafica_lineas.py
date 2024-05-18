import turtle

t = turtle.Turtle()
t.speed(3)
datos = [10,40,80,50,90,30,90,40]
t.penup()
t.goto(-200,-150)
t.pendown()
t.left(90)
for valor in datos:
    t.goto(t.xcor()+40, valor-150)
turtle.done()