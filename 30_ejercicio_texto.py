import turtle
t = turtle.Turtle()
t.speed(2)
def crear_texto(mensaje,color):
    t.fillcolor(color)
    t.begin_fill()  
    t.penup()
    t.goto(-120,80)  
    t.pendown()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.write(mensaje, align="center",font=("Arial",24,"bold"))
crear_texto("@josecodetech","lightblue")
turtle.done()