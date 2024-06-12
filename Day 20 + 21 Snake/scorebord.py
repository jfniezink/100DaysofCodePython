from turtle import Turtle

STIJL = ('Courier', 10)

class ScoreBoard(Turtle):    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.color("white")
        self.write(f"score = {self.score}", move=False, align="center", font=STIJL)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(
            f"Game Over! final score = {self.score}", 
            move=False, 
            align="center", 
            font=("Courier", 20, "bold"))