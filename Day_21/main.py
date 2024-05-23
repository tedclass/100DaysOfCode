import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()




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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detecting wall collisions 
    if ball.ycor() > 295 and ball.xcor() > 295 or ball.ycor() < -295 and ball.xcor() < -295:
        ball.bounce_y()
        
        
    #detect collisions with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 295 or ball.distance(l_paddle) < 50 and ball.xcor() < -295:
        ball.bounce_x()
        #ball.bounce_y()

    #Detecting when the right paddle misses
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.l_point()
        
        
    #Now for the left side
    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()