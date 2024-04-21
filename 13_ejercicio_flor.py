import turtle

def dibuja_petalo():
    t.circle(50,60)
    t.left(120)
    t.circle(50, 60)
    t.left(120)
def dibuja_flor(petalos):
    for _ in range(petalos):
        dibuja_petalo()
        t.left(360/petalos)
if __name__ == '__main__':
    t = turtle.Turtle()
    t.speed(3)
    t.color('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    dibuja_flor(4)
    t.end_fill()
    turtle.done()
    