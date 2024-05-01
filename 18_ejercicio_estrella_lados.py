import turtle
t = turtle.Turtle()
num_lados = int(input("Dime el numero de lados de la estrella: "))
t.speed(1)
angulo = 180 - (180/num_lados)
for _ in range(num_lados):
    t.forward(100)
    t.right(angulo)
turtle.done()