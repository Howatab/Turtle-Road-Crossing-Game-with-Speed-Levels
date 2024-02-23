from turtle import Turtle
from scoreboard import Scoreboard


STARTING_POSITION = (0, -330)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 310


class Player:
    def  __init__(self) -> None:
        self.Player = Turtle()
        self.Player.seth(90)
        self.Player.shapesize(1.4,1.4)
        self.Player.shape("turtle")
        self.Player.color('aquamarine')
        self.Player.penup()
        self.Player.goto(STARTING_POSITION)
        self.scoreboard = Scoreboard()
    
    def Move_up(self):
        self.Player.forward(50)
            
    def Move_down(self):
        if self.Player.ycor() > STARTING_POSITION[1]:
            self.Player.sety(self.Player.ycor()-50)
            
    def Move_left(self):
        if self.Player.xcor() > -450:
            self.Player.setx(self.Player.xcor()-50)
            
    def Move_right(self):
        if self.Player.xcor() < 450:
            self.Player.setx(self.Player.xcor()+50)
            
    def reset(self):
        self.Player.setpos(STARTING_POSITION)
        
    def position(self):
        return self.Player.pos()
    
    def positiony(self):
        return self.Player.ycor()
    
    def Level_clear(self):
        if self.Player.ycor()>310:
            self.scoreboard.increase_level()
            self.reset()