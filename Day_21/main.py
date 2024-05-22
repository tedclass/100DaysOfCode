import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

#Setting up the screen enviroment 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong 1998!!")
screen.tracer(0)

#Creating the two paddles
r_paddle = Paddle((300, 0))
l_paddle = Paddle((-300, 0))
ball = Ball()




screen.listen()
#Movement for the two paddle
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
#for the left paddle
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


#This continuosly updates the screen as long as the game is ongoing
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detecting wall collisions 
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce()
        
    #detect collisions with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce()

screen.exitonclick()