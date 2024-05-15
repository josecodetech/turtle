import turtle
t = turtle.Turtle()
t.speed(3)
parar = True
def comenzar(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def parar(x,y):
    global parar
    if parar:
        t.penup()
        parar = False
    else:
        t.pendown()
        parar = True
def dibujar(x,y):
    t.goto(x,y)
turtle.onscreenclick(comenzar, 1)
turtle.onscreenclick(parar,3)
turtle.onscreenclick(dibujar)
turtle.done()
    