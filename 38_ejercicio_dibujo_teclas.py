import turtle
t = turtle.Turtle()
t.speed(4)
t.pensize(4)
t.color("orange")
def adelante():
    t.setheading(90)
    t.forward(20)
def atras():
    t.setheading(270)
    t.forward(20)
def izquierda():
    t.setheading(180)
    t.forward(20)
def derecha():
    t.setheading(0)
    t.forward(20)
turtle.onkey(adelante, "Up")
turtle.onkey(atras, "Down")
turtle.onkey(izquierda,"Left")
turtle.onkey(derecha,"Right")
turtle.listen()
turtle.done()
# turtle.exitonclick()
