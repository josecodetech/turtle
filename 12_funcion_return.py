import turtle

def dame_area(ancho, alto):
    area = ancho * alto
    return area
if __name__ == "__main__":
    ancho = 10
    alto = 2
    area = dame_area(ancho, alto)
    print("El valor del area es : ", area)
    t = turtle.Turtle()
    t.speed(3)
    t.color="red"
    t.circle(area)
    turtle.done()