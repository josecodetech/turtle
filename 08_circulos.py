import turtle

def dibuja_circulo(x,y, radio):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.circle(radio)
if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(2)
    t.color("green")
    radio = 200
    for _ in range(10):
        dibuja_circulo(0,0,radio)
        radio -= 20
    turtle.done()