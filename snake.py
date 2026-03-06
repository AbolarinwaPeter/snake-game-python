import turtle

class Snake:
    def __init__(self):
        self.head = None
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        snake_length = 3
        for i in range(snake_length):
            coordinates = (-20*i, 0)
            self.add_segment(coordinates)
        self.head = self.snake_body[0]
    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        self.snake_body.append(new_segment)
        new_segment.goto(position)
    def extend(self):
        self.add_segment(self.snake_body[-1].pos())


    def detect_collision(self):
        for segment in self.snake_body[1:]:
            # print("collision: ", self.snake_body.index(segment))
            if self.head.distance(segment) < 15:
               return True


    def move(self):
        foot_print = self.head.pos()
        self.head.forward(20)
        for segment in self.snake_body[1:]:
            seg_print = segment.pos()
            segment.goto(foot_print)
            foot_print = seg_print
    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def face_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def face_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def reset_snake(self):
        for seg in self.snake_body[3:]:
            seg.hideturtle()
        self.snake_body = self.snake_body[:3]
        self.head.home()