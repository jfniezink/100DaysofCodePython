import turtle as t
import random

def random_color() -> tuple:
    """Creates a random RGB color. Return a tuple containing R, G and B"""
    t.colormode(255)
    r,g,b = random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)
    return r,g,b


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.reset()


def big_pen():
    t.pensize(10)


def change_color():
    t.colormode(255)
    t.pencolor(random_color())


def Etch_a_Sketch():
    """Starts Turtle graphic with inputs w,a,s,d to move the turtle. 
    c for reset the canvas
    space for random color change"""
    t.listen()
    t.onkey(key="w", fun=move_forward)
    t.onkey(key="s", fun=move_backward)
    t.onkey(key="a", fun=turn_left)
    t.onkey(key="d", fun=turn_right)
    t.onkey(key="c", fun=clear)
    t.onkey(key="x", fun=big_pen)
    t.onkey(key="space", fun=change_color)
    t.mainloop()


def turtle_race():
    import turtle as t
    import random
    """Creates 6 turtles to race from point -350 to 350. returns the winnen of the race"""
    # set screen parameters
    t.title("Turtle Racing!")

    racers = []
    positions = []
    colors = ["red","green", "blue", "purple", "yellow", "orange"]
    Guessed_winner = t.textinput("Choose a winner", 'Pick a color: "red","green", "blue", "purple", "yellow", "orange"').lower()
    # Create 6 turtles
    for _ in range(len(colors)):
        racers.append(t.Turtle(shape="turtle"))
    
    # Set speed to fast for all turtles
    for racer in racers:
        racer.speed("fastest")
    
    # Set colors for all turtles and move to start position (-350)
    for racer in racers:
        racer.penup()
        racer.color(colors[racers.index(racer)])
        positie = racer.position()
        racer.setposition(positie[0],positie[1] + (50 * racers.index(racer)))
        racer.setheading(180)
        racer.forward(350)
        racer.setheading(0)
        positions.append(racer.position()[0])
    
    # Race turtles for random forward movement to point 350
    while max(positions) < 350.0:
        for racer in racers:
            racer.forward(random.randint(1,5))
            positions[racers.index(racer)] = racer.position()[0]
    
    # Declare winner based on first turtle to get to point 350
    winner = colors[positions.index(max(positions))]
    if winner == Guessed_winner:
        print(f"you win! {Guessed_winner} is indeed the winner")
    else:
        print(f"you lose! {winner} is the winner!")


Etch_a_Sketch()