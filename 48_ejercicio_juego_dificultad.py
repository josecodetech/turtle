import turtle
import random
import time

screen = turtle.Screen()
screen.title("Captura la tortuga")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)
score = 0
# Mostrar puntuacion
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,260)
score_display.write(f"Puntos: {score}",align="center", font=("Arial", 24, "normal"))
# Temporizador
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, 230)
tiempo = 30
velocidad = 1

# funcion nivel de dificultad
def pon_nivel(nivel):
    global tiempo, velocidad
    if nivel == "facil":
        tiempo = 60
        velocidad = 2
    elif nivel == "medio":
        tiempo = 30
        velocidad = 3
    elif nivel == "pro":
        tiempo = 15
        velocidad = 5
    t.speed(velocidad)
    actualizar_tiempo()
    mover()

def mover():
    x = random.randint(-390,390)
    y = random.randint(-290, 290)
    t.goto(x,y)
def capturar(x,y):
    global score
    score += 1 # score = score + 1
    score_display.clear()
    score_display.write(f"Puntos: {score}", align="center", font=("Arial", 24, "normal"))
    mover()
def actualizar_tiempo():
    global tiempo
    if tiempo > 0:
        tiempo -= 1
        timer_display.clear()
        timer_display.write(f"Tiempo: {tiempo} s", align="center", font=("Arial", 24, "normal"))
        screen.ontimer(actualizar_tiempo, 1000)
    else:
        terminar()
def terminar():
    t.hideturtle()
    screen.onscreenclick(None) #desactivamos clicks
    timer_display.clear()
    timer_display.write(f"Fin del juego. Puntos: {score}", align="center", font=("Arial", 24, "normal"))       
# iniciamos el juego
turtle.onscreenclick(capturar)
dificultad = screen.textinput("Dificultad", "Selecciona la dificultad: facil, medio, pro")
if dificultad:
    pon_nivel(dificultad)

# mover()
# actualizar_tiempo()
turtle.done()    