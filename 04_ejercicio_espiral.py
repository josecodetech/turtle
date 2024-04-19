import turtle
t = turtle.Turtle()
longitud = 10 
for _ in range(50):
    t.forward(longitud)
    t.left(90)
    longitud +=5
turtle.done()