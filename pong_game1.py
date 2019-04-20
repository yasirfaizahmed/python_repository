#pong game 1 by: yasir faiz ahmed
#using turtle built_in module with python3.0

#Window
import turtle
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=1000 , height=600)
window.title("pong game")
window.tracer()
#paddle_a
paddle_a = turtle.Turtle()
paddle_a.color("green")
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450,0)
#paddle_b
paddle_b = turtle.Turtle()
paddle_b.color("green")
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5 , stretch_len=1)
paddle_b.penup()
paddle_b.goto(450,0)
#ball
ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dy = 4
ball.dx = 4
#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y+20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y = y-20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y = y+20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y = y-20
    paddle_b.sety(y)
#keyboard bindings
window.listen()
window.onkeypress(paddle_a_up,"q")
window.onkeypress(paddle_a_down,"a")
window.onkeypress(paddle_b_up,"w")
window.onkeypress(paddle_b_down,"s")
#main game loop
while True:
    window.update()
    #moving the ball
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy = ball.dy*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy = ball.dy*-1
    if ball.xcor()>490:
        ball.goto(0,0)
    if ball.xcor()<-490:
        ball.goto(0,0)
    #collision with paddles
    if ball.xcor()>430 and ball.ycor()<paddle_b.ycor()+50:
        ball.dx = ball.dx*-1
    if ball.xcor()<-430 and ball.ycor()<paddle_a.ycor()+50:
        ball.dx = ball.dx*-1
