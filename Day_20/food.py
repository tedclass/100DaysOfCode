from turtle import Turtle
import random

class Food(Turtle):#Giving the food class all the possible options from turtle 
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5) #tHIS MULTIPLIES THE ACTUAL SIZE VALUE BY THE STRETCH VALUE
        self.color('red')
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)