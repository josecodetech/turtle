import turtle
t = turtle.Turtle()
colores = ['red','orange','yellow','green','blue','indigo','violet']
t.speed(1)
for i in range(len(colores)):
    t.color(colores[i])
    t.width(i+1)
    t.circle(20*(i+1))
turtle.done()