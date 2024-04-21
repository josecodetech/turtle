import turtle

t = turtle.Turtle()
# velocidad de dibujo con speed
t.speed(2)
for _ in range(4):
    t.forward(100)
    t.left(90)

# retrasando con delay
turtle.delay(50) #milisegundos
t.circle(100)
turtle.done()