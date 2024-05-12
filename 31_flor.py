import turtle
t = turtle.Turtle()
t.speed(4)
def petalo():
    t.circle(50,60)
    t.left(120)
    t.circle(50,60)
    t.left(120)
for _ in range(6):
    petalo()
    t.left(60)
turtle.done()