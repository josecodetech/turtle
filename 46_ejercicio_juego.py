import turtle
import random

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
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,260)
score_display.write(f"Puntos: {score}",align="center", font=("Arial", 24, "normal"))
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
turtle.onscreenclick(capturar)
mover()
turtle.done()    