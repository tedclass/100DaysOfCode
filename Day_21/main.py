from turtle import Screen, Turtle


#Setting up the screen enviroment 
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong 1998!!")
screen.tracer(0)


#Creating a paddle 
paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_len=1,stretch_wid=5)
paddle.penup()
paddle.goto(350, 0)

#Function to move the paddle up
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(),new_y)


#Function to move the paddle down
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")


#This continuosly updates the screen as long as the game is ongoing
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()