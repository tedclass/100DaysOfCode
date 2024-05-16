from turtle import Turtle
#Getting rid of hard coded sections
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score_board()
        
    def update_score_board(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT) 
        
    def increase_score(self):
        #clear score first 
        self.score +=1
        self.clear()
        self.update_score_board()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over! You suck!!!", align=ALIGNMENT,font=FONT)