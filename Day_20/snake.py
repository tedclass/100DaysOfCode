from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #This sets the inital position/conditions for the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
            
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
            
        

    def extend(self):
        #adding a new segment \
        self.add_segment(self.segments[-1].position())
        
    
    
#This is how the snake moves
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
# Up direction 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

# down direction
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

# left direction
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
# Right direction            

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
