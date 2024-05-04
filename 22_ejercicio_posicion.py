import turtle

numero_lados = int(input("Ingresa el numero de lados: "))
angulo = 360 / numero_lados
tamaño = min(turtle.window_width(), turtle.window_height()) * 0.2
t = turtle.Turtle()
t.penup()
t.speed(1)
t.goto(-50, -tamaño / 3)
t.pendown()
for _ in range(numero_lados):
    t.forward(tamaño)
    t.left(angulo)
t.hideturtle()
turtle.done()
