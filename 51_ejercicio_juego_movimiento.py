import turtle
import random
import time
import pygame
# iniciamos pygame para sonido
pygame.init()
sonido = pygame.mixer.Sound("golpe.mp3")
screen = turtle.Screen()
screen.title("Captura la tortuga")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("green")
# t.penup()
# t.speed(0)
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
colores_fondo = ['lightblue','lightgreen','lightyellow','lightcoral']
color_tortuga = ['green','blue','red','purple','orange']
tortugas = []
def crear_tortugas(cantidad,velocidad):
    for i in range(cantidad):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(random.choice(color_tortuga))
        t.penup()
        t.speed(velocidad)
        t.goto(random.randint(-390, 390), random.randint(-290, 290))
        t.setheading(random.randint(0, 360))
        tortugas.append((t,random.randint(1,10)))
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
    # t.speed(velocidad)
    actualizar_tiempo()
    return velocidad
    # mover(t)

def mover(t):
    # x = random.randint(-390,390)
    # y = random.randint(-290, 290)
    # t.goto(x,y)
    t.forward(10)
    if t.xcor() > 390 or t.xcor() < -390:
        t.right(180)
    if t.ycor() > 290 or t.ycor() < -290:
        t.right(180)
def capturar(x,y):
    global score
    for t, valor in tortugas:
        if t.distance(x, y) < 20:
            score +=1 # score = score + 1
            # t.hideturtle()
            mover(t)
    # score += 1 # score = score + 1
            score_display.clear()
            score_display.write(f"Puntos: {score}", align="center", font=("Arial", 24, "normal"))
            sonido.play(maxtime=500) # reproducimos el sonido
            
            # sonido.stop()
            screen.bgcolor(random.choice(colores_fondo))
            # mover()
            break
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
    for t, _ in tortugas:        
        t.hideturtle()
    screen.onscreenclick(None) #desactivamos clicks
    timer_display.clear()
    timer_display.write(f"Fin del juego. Puntos: {score}", align="center", font=("Arial", 24, "normal"))      
    screen.textinput("Fin del juego", "Presiona enter para reiniciar")
    comenzar_juego()
def comenzar_juego():
    for t, _ in tortugas:        
        t.hideturtle()
    global score, tiempo, cantidad, velocidad
    score = 0
    tiempo = 30
    score_display.clear()
    score_display.write(f"Puntos: {score}", align="center", font=("Arial", 24, "normal"))
    
    dificultad()
    # actualizar_tiempo()
    screen.onscreenclick(capturar)
    turtle.onscreenclick(capturar)
def dificultad():
    dificultad = screen.textinput("Dificultad", "Selecciona la dificultad: facil, medio, pro")
    if dificultad:
        cantidad = 10
        velocidad = pon_nivel(dificultad)
        crear_tortugas(cantidad,velocidad)  

if __name__ == "__main__":    
    # iniciamos el juego
    comenzar_juego()
    # turtle.onscreenclick(capturar)
    # dificultad()
    # actualizar_tiempo()
    # mover()
    # actualizar_tiempo()
    turtle.done() 