from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speeds = 3

    def spawn_car(self):
        random_chance = random.randint(1, 9)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            randy = random.randint(-250, 250)
            new_car.goto(300, randy)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.speeds)

    def increase_speed(self):
        self.speeds += 1
