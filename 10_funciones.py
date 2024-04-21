import turtle

def dibuja_cuadrado():
    t.color("red")
    for _ in range(4):
        t.forward(100)
        t.left(90)
        
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(3)
    dibuja_cuadrado()
    turtle.done()