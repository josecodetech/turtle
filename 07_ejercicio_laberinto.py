import turtle

def dibuja_pared():
    t.pendown()
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.backward(80)
    t.right(90)
    t.penup()
def mover_sin_dibujar(x,y):
    t.penup()
    t.goto(x,y)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    mover_sin_dibujar(-200, 200)
    t.pendown()
    for _ in range(5):
        for _ in range(4):
            dibuja_pared()
        t.penup()
        mover_sin_dibujar(-200, t.ycor() - 120)
    mover_sin_dibujar(-200,200)
    t.right(90)
    for _ in range(6):
        dibuja_pared()
        t.forward(40)
    mover_sin_dibujar(-180,180)    
    turtle.done()