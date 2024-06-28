import turtle
import random

STARTING_MOVE_DISTANCE = 2
RANDOMCHANGE = 6

play = 'Day 23 Turtle Crossing\Shapes\shape1.gif'

shapes = ['Day 23 Turtle Crossing\Shapes\shape1.gif',
          'Day 23 Turtle Crossing\Shapes\shape2.gif',
          'Day 23 Turtle Crossing\Shapes\shape3.gif',
          'Day 23 Turtle Crossing\Shapes\shape4.gif',
          'Day 23 Turtle Crossing\Shapes\shape5.gif',
          'Day 23 Turtle Crossing\Shapes\shape6.gif'
          ]

for shape in shapes:
    turtle.register_shape(shape)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_increment = 0

    def make_car(self):
        random_chance = random.randint(1, RANDOMCHANGE)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.shape(random.choice(shapes))
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            random_y = random.randint(-245, 245)
            new_car.goto(310, random_y)

            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.move_increment)

            if car.xcor() < -400:
                car.hideturtle()

    def increase_speed(self):
        self.move_increment += 1