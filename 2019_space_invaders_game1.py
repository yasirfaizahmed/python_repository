#LIBRARIES
import turtle
import random
#WINDOW
window = turtle.Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.tracer(0)
window.title("-----SPACE INVADERS----")
#SHIP
ship = turtle.Turtle()
ship.speed(0)
ship.penup()
ship.shape("triangle")
ship.color("gray")
ship.goto(0, -200)
ship.tilt(90)
ship.shapesize(stretch_len= 2, stretch_wid= 1)
#ENEMY
enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
enemy.shape("circle")
enemy.color("red")
enemy.setx(-250)
enemy.sety(250)
enemy_speed = 0.2
#BULLET
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.speed(0)
bullet.shapesize(stretch_len=0.5, stretch_wid=0.3)
bullet.color("white")
bullet.tilt(90)
bullet.goto(0, 0)
bullet.penup()
bullet.hideturtle()
bullet_state = "ready"
#SCORE
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(60,250)
pen.write("Score:{}".format(score), align="center", font=("Courier", 24, "normal"))
#BOUNDARY
level = 150
bound = turtle.Turtle()
bound.shape("square")
bound.color("white")
bound.shapesize(stretch_wid=0.1, stretch_len=100)
bound.penup()
#bound.speed(0)
bound.setposition(0, level)
#MOVEMENT FUNCTIONS
def go_left():
    if ship.xcor()>=-280:
        x = ship.xcor()
        x = x - 15
        ship.setx(x)
def go_right():
    if ship.xcor()<=265:
        x = ship.xcor()
        x = x + 15
        ship.setx(x)
def fire():
    global bullet_state
    bullet.showturtle()
    bullet.setposition(ship.xcor(), ship.ycor() + 10)
def ex_i():
    pen.clear()
    pen.write("-------game over-------",align = "center", font = ("Courier", 24, "normal"))
    enemy.hideturtle()
#KEY BINDINGS
window.listen()
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")
window.onkeypress(fire, "space")
#RANDOM SPAWNING OF ENEMY
rand_num = random.randint(4, 7)
while rand_num>=0:
    rand_x = random.randint(-280, 280)
    rand_y = random.randint(150, 280)
    rand_enemy = turtle.Turtle()
    rand_enemy.color("red")
    rand_enemy.penup()
    rand_enemy.goto(rand_x, rand_y)
    rand_enemy.shape("circle")
    rand_enemy.speed(0)
    rand_num-=1
#MAIN LOOP
while True:
    window.update()
    x = enemy.xcor()+enemy_speed
    enemy.setx(x)
    if enemy.xcor()>280:
        enemy_speed = enemy_speed*-1
        enemy.sety(enemy.ycor() - 20)
    if enemy.xcor()<-280:
        enemy_speed = enemy_speed*-1
        enemy.sety(enemy.ycor() - 20)
    if bullet_state=="ready":
        y = bullet.ycor()
        y = y + 2
        bullet.sety(y)
    if enemy.distance(bullet)<=10:
        score +=1
        pen.clear()
        pen.goto(60, 250)
        pen.write("Score:{}".format(score), align="center", font=("Courier", 24, "normal"))
        enemy.hideturtle()
        enemy.goto(-250, 250)
        enemy.showturtle()
    if enemy.ycor()<=160:
        ex_i()

