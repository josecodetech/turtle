import turtle

t = turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("lightblue")
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()
turtle.done()