import turtle
import random
import time
#starting the timer
start = time.time()
#score
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score:", align="center",font=("Courier",24,"normal"))
#window
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("turtle methods test1")
screen.setup(width=600,height=600)
#body
body= turtle.Turtle()
body.color("red")
body.shape("circle")
body.penup()
body.goto(-100,0)
body.direction = "none"
body.speed(0)
#ground
ground = turtle.Turtle()
ground.color("black")
ground.shape("square")
ground.shapesize(stretch_len=100,stretch_wid=0.1)
ground.penup()
ground.goto(0,-14)
ground.speed(0)
#obstacle1
obsta1 = turtle.Turtle()
obsta1.color("black")
obsta1.shape("square")
obsta1.penup()
obsta1.speed(0)
obsta1.goto(300, -2)
obsta1.dx = 4
#obstacle2
obsta2 = turtle.Turtle()
obsta2.color("gray")
obsta2.shape("square")
obsta2.penup()
obsta2.speed(0)
obsta2.goto(600,-2)
obsta2.dx = 4
#moving obstacles
def obsta_move():
    map(score,0,50,)
    obsta1.setx(obsta1.xcor() - obsta1.dx)
    obsta2.setx(obsta2.xcor() - obsta2.dx)
    if obsta1.xcor()<=-290:
        obsta1.goto(x1,-2)
    if obsta2.xcor()<=-290:
        obsta2.goto(x2,-2)

#move
def move():
    body.direction = "up"
#touch
def touched():
    if (body.distance(obsta1)<=20 or body.distance(obsta2)<=20):
        end = time.time()
        exit(print("run time=", end-start))
#keyboard bindings
screen.listen()
screen.onkeypress(move,"w")
#main loop
while True:
    screen.update()
    touched()
    #jump
    if body.direction =="up":
        while body.ycor()<=60:
            touched()
            body.sety(body.ycor() + 4)
            obsta1.setx(obsta1.xcor() - 5)
            obsta2.setx(obsta2.xcor() - 5)
            if body.ycor()==60:
                break
        if body.ycor() == 60:
            while body.ycor() >= 0:
                touched()
                body.sety(body.ycor() - 4)
                obsta1.setx(obsta1.xcor() - 5)
                obsta2.setx(obsta2.xcor() - 5)
                body.direction = "none"
            pen.clear()
            pen.write("Score:{}".format(score), align="center", font=("Courier", 24, "normal"))
            score = score + 1
    obsta_move()
    x1 = random.randint(200, 350)
    x2 = random.randint(500, 600)