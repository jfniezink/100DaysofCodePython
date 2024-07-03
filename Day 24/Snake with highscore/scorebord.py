from turtle import Turtle

STIJL = ('Courier', 10)


class ScoreBoard(Turtle):    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        with open("Day 24\Snake with highscore\data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Score = {self.score}, Highscore = {self.high_score}", move=False, align="center", font=STIJL)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("Day 24\Snake with highscore\data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard

    # def gameover(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(
    #         f"Game Over! final score = {self.score}", 
    #         move=False, 
    #         align="center", 
    #         font=("Courier", 20, "bold"))