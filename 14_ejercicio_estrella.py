import turtle

def dibuja_estrella(tamaño):
    for _ in range(5):
        t.forward(tamaño)
        t.right(144)
def dibujar_estrellas_concentricas(num_estrellas):
    for i in range(num_estrellas):
        dibuja_estrella(25*(i+1))
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.right(360/num_estrellas)
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(3)
    dibujar_estrellas_concentricas(8)
    turtle.done()