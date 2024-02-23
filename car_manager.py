import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
STARTING_XPOSITION = 500
ROAD_LINES = []



class CarManager:
    def __init__(self,Cars) -> None:
        self.Cars = []
        self.No_of_cars = Cars
        self.speed = STARTING_MOVE_DISTANCE
        CarManager.road_lines()
        self.CarCrossed = False
        self.collision = False
        self.Create_cars()
        
    @staticmethod
    def road_lines():
        for i in range (-270,300):
            if i % 50 == 0:
                ROAD_LINES.append(i-25)
                
                
    def Create_cars(self):
        for _ in range(self.No_of_cars):
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.teleport(random.randint(-500,500),random.choice(ROAD_LINES))
            car.setheading(180)
            self.Cars.append(car)
        
    def Car_move(self,turtle):
        for car in self.Cars:
            car.forward(self.speed)
            CarManager.Car_cross_check(car)
            self.CollisionCheck(car,turtle)
            
    @staticmethod
    def Car_cross_check(car):
        if car.xcor()<-500:
            car.goto(STARTING_XPOSITION,random.choice(ROAD_LINES))
            
            
            
    def CollisionCheck(self,car,turtle):
        if car.distance(turtle) < 20:
            self.collision = True