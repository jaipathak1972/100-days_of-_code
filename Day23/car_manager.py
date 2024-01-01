from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.carss = []
        self.car_speed = STARTING_MOVE_DISTANCE 
        self.size_len = random.randint(1, 3)
        self.number = 20
        self.hideturtle()

        for _ in range(self.number):
            car = Turtle()
            car.penup()
            
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=0.8, stretch_len=1.5)
            car.setheading(180)  # Set the initial direction to the left
            car.goto(random.randint(-280, 380), random.randint(-240, 280))
            self.carss.append(car)

    def move_cars(self):
        for car in self.carss:
            car.forward(self.car_speed)

            if car.xcor() < -320:

                car.goto(random.randint(320 ,500), random.randint(-240, 240))  # Reset the car's position
                self.number += 1
    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
    
    