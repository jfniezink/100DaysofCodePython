import pandas as pd
import turtle
from PIL import Image
import time

# get image width and height
image_width, image_height = Image.open('blank_states_img.gif').size

# Setup the screen
screen = turtle.Screen()

# setup title and icon
screen.title("Name the states")
screen.setup(width=image_width, height=image_height)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

# create game functionality

df = pd.read_csv("50_states.csv")
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
states_list = df["state"].to_list()

while len(states_list) != 0:
    time.sleep(0.05)
    screen.update()    
    user_input = screen.textinput(title=f"{50-len(states_list)}/50 guessed.", prompt="Guess a state or type 'exit' to exit").title()
    if user_input in states_list:
        x_cor = df[df["state"] == user_input]["x"].to_list()[0]
        y_cor = df[df["state"] == user_input]["y"].to_list()[0]
        writer.goto(x_cor,y_cor)
        writer.write(arg=user_input,align="left")
        states_list.remove(user_input)
    elif user_input == 'Exit':
        break    

if len(states_list) == 0:
    writer.goto(0,0)
    writer.write(arg="You win, you guessed all the states! good job",align="center")
else:
    pd.DataFrame({"States to learn": states_list}).to_csv("States_to_Learn.csv", index=False)

screen.exitonclick()