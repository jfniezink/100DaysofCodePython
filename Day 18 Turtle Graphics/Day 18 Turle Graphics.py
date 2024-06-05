#import modules
import turtle as t
import random
import colorgram


def random_color() -> tuple:
    """Creates a random RGB color. Return a tuple containing R, G and B"""
    t.colormode(255)
    r,g,b = random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)
    return r,g,b


def draw_spirograph(size_of_gap:int) -> None:
    """Creates a Turtle spirograph with random color circles.
    Sets speed to max to draw. When done it resets speed to before"""
    speed_before = t.speed()
    t.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
    t.speed(speed_before)
    t.exitonclick()


def random_walk(counter:int) -> None:
    """Creates a random walk for the turtle. Loops through given input for pencolor, forward and set heading."""
    direction = [0,90,180,270]
    for i in range(counter):
        t.pencolor(random_color())
        t.forward(random.randint(0,50))
        t.setheading(random.choice(direction))
    t.exitonclick()


def draw_angles(num:int):
    """Draw triangle, rectangle etc until given input"""
    for i in range(3,num):
        t.pencolor(random_color())
        for j in range(i):
            t.forward(100)
            t.right(360 / i)
    t.exitonclick()


def get_colorgram(img:str,num:int) -> list:
    colors = colorgram.extract(img,num)
    return colors


def draw_dot_painting(num_of_dots:int,dot_size:int,space_between:int) -> None:
    """Uses Turtle module to print a dotted painting. Takes a number for the painting.
    Painting wil be num by num dots. """
    t.speed("fastest")
    t.screensize(num_of_dots*space_between,num_of_dots*space_between)
    t.colormode(255)
    t.hideturtle()
    t.penup()
    t.setheading(225)
    t.forward(num_of_dots * space_between)
    t.setheading(0)
    positie = t.position()

    for _ in range(num_of_dots):
        t.setposition(positie[0],positie[1]+(space_between*_))
        for i in range(num_of_dots):
            t.dot(dot_size,random_color())
            t.forward(space_between)


t.mainloop()