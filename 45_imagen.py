import turtle

screen = turtle.Screen()
screen.addshape("turtle.gif")
t = turtle.Turtle()
t.speed(1)
t.shape("turtle.gif")
t.penup()
t.goto(-100,0)
t.pendown()
t.forward(300)
turtle.done()