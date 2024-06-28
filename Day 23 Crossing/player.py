import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 275

turtleshape = "Day 23 Turtle Crossing\Shapes\squirrle.gif"
turtle.register_shape(turtleshape)

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(turtleshape)
        self.penup()
        self.shapesize(2,2,1)
        self.setheading(90)
        self.go_to_start()

    def moveup(self):
        self.forward(MOVE_DISTANCE)

    def movedown(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False