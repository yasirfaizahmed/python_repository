import turtle
import time
import random

delay = 0.05

            #setting up the screen
window = turtle.Screen()
window.title("snake game")
window.bgcolor("black")
window.setup(width=600 , height=600)
window.tracer(0)                #turns off animation(screen updates)


           #snake head
head = turtle.Turtle()          #creates a object
head.speed(0)                   #speed of animation , 0 is the fastestone
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)                  #snake head starts at the center of the screen(x=0,y=0)
head.direction = "stop"

           #food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,200)

segments = []

           #funcions
def move():
    if head.direction =="up":
        y = head.ycor()         #declaring y var as y coordinate of head
        head.sety(y+20)         #moves at speed of 20 pixels
    if head.direction == "down":
        y = head.ycor()         # declaring y var as y coordinate of head
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()         # declaring x var as x coordinate of head
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()         # declaring x var as x coordinate of head
        head.setx(x+20)

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

         #keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


          #main game loop
while True:
    window.update()             #updates screen
    if head.distance(food)<20:  #calculates the distance between two turtles
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)          #moves the food to randomly generated x,y cors



    move()                      # calling method move
    time.sleep(delay)