import turtle 
def dibuja_poligono(lados):
    angulo = 360 / lados
    for _ in range(lados):
        t.forward(100)
        t.left(angulo)

if __name__ == "__main__":
    t = turtle.Turtle()
    dibuja_poligono(8)
    turtle.done()