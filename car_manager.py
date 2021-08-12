from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.level = 2
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for index in range(50):
            car = Turtle(shape="square")
            car.penup()
            car.setheading(180)
            car.goto(x=random.randint(300, 2500), y=random.randint(-240, 240))
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            self.cars.append(car)

    def move(self, score):
        if score.level == self.level:
            self.move_distance = self.move_distance + MOVE_INCREMENT
            self.level += 1
        for car in self.cars:
            car.forward(self.move_distance)

    def restart_position(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(x=random.randint(300, 2000), y=random.randint(-240, 240))

    def check_collision(self, player):
        for car in self.cars:
            if car.distance((player.xcor() + 5), player.ycor()) < 20:
                return True
