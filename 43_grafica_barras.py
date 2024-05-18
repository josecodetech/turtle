import turtle
t = turtle.Turtle()
t.speed(3)
datos = [120,56,42,89,34,23,95,160,190]
def grafica_barras(altura):
    t.begin_fill()
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()
t.penup()
t.goto(-200,-150)
t.pendown()
for valor in datos:
    grafica_barras(valor)
    t.penup()
    t.forward(15)
    t.pendown()
turtle.done()