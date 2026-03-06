import turtle
import time
import snake
import food
import score_board
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)
snake = snake.Snake()
food = food.Food()
score_board = score_board.ScoreBoard()
def restart_game():
    global game_on
    if not game_on:
        game_on = True
        snake.reset_snake()
        score_board.reset_score()
        food.refresh()
        start_game()

def start_game():
    global game_on
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()
        if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
            game_on = False
            score_board.game_over()
        if snake.detect_collision():
            game_on = False
            score_board.game_over()
screen.onkey(key= "Up", fun= snake.face_up)
screen.onkey(key= "Down", fun= snake.face_down)
screen.onkey(key= "Left", fun = snake.turn_left)
screen.onkey(key= "Right", fun = snake.turn_right)
screen.onkey(key= "space", fun = restart_game)

game_on = True
start_game()
screen.exitonclick()