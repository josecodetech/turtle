import turtle
t = turtle.Turtle()
t.speed(2)
def mover_adelante():
    t.forward(10)
def mover_atras():
    t.backward(10)
def girar_izquierda():
    t.left(10)
def girar_derecha():
    t.right(10)
turtle.onkey(mover_adelante,"w")
turtle.onkey(mover_atras,"s")
turtle.onkey(girar_izquierda,"a")
turtle.onkey(girar_derecha,"d")
turtle.listen()
turtle.done()