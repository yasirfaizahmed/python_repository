import turtle

screen = turtle.Screen()#creates a window object called screen
screen.bgcolor("black")#gives the bg color as black
screen.title("turtle methods test1")#title as discribed
screen.setup(width=600,height=600)#setup gives the height and width

object = turtle.Turtle()#creating a turtle object called object
object.color("blue")#giving turtle a blue color
object.shape("triangle")
object.penup()
object.goto(0,0)

def left():
    object.direction = "left"
def right():
    object.direction = "right"
def up():
    object.direction = "up"
def down():
    object.direction = "down"

def move():
    if object.direction=="left":
        x = object.xcor()
        object.setx(x-20)
    if object.direction=="right":
        x = object.xcor()
        object.setx(x+20)
    if object.direction=="up":
        y = object.ycor()
        object.sety(y+20)
    if object.direction=="down":
        y = object.ycor()
        object.sety(y-20)

screen.listen()
screen.onkeypress(left,"a")
screen.onkeypress(right,"d")
screen.onkeypress(up,"w")
screen.onkeypress(down,"s")


while 1==1:#loop for updating the declared screen
    screen.update()#updates the screen as well as the whole turtle objects created
    move()
