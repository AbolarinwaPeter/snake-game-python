import turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt", mode= "r") as file:
    high_score = file.read()
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = int(high_score)
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as u_file:
                u_file.write(f"{self.high_score}")
        self.update_scoreboard()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset_score(self):
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()
