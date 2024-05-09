import turtle
t = turtle.Turtle()
t.speed(2)
turtle.bgcolor("blue")
t.color("red")
for _ in range(4):
    t.forward(100)
    t.left(90)
t.color("yellow")
t.circle(100)
turtle.done()