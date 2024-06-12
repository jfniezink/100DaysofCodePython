from turtle import Screen
import time
from snake import Snake
from food import Food
from scorebord import ScoreBoard

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

# 
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
    
    # detect collision with wall
    game_over_conditions = [
                                screen.window_height() / 2 * -1,
                                screen.window_height() /2,
                                screen.window_width() / 2, 
                                screen.window_width() / 2 * -1
                            ]   
    if snake.head.position()[1] in game_over_conditions or snake.head.position()[0] in game_over_conditions:
        game_is_on = False
        scoreboard.gameover()
    
    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
        
screen.exitonclick()