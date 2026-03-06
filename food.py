import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))