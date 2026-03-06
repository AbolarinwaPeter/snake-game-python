import turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset_score(self):
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()