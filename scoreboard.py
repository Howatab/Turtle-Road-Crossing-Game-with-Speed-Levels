from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard:
    def __init__(self) -> None:
        self.level = 0
        self.pen = Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.color('black')
        self.pen.goto(-450,320)
        self.display_level()
        
    def increase_level(self):
        self.level += 1
        self.display_level()
    
    def display_level(self):
        self.pen.clear()
        self.pen.write(f"Level = {self.level}",font=FONT)
        
    def Display_Gameover(self):
        self.pen.goto(0,0)
        self.pen.color('red')
        self.pen.write(f"GAME OVER",font=FONT)
        
        