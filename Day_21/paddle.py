from turtle import Turtle

class Paddle(Turtle):#Creating a child class from turtle to create paddles
        def __init__(self,position):
            super().__init__()
            self.shape('square')
            self.color('white')
            self.shapesize(stretch_len=1,stretch_wid=5)
            self.penup()
            self.goto(position)
            
        # #Function to move the self up
        def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)


#Function to move the self down
        def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
