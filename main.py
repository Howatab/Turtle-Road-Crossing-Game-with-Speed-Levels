
import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('dim gray')
screen.setup(width=1000, height=700)
road_sizex = screen.window_width()/2
road_sizey = screen.window_height()/2
screen.tracer(0)

def draw_board():
    Road = Turtle()
    Road.hideturtle()
    Road.color('azure')
    Road.width(8)
    Yellow_line = Turtle()
    Yellow_line.hideturtle()
    Yellow_line.color('orange')
    Yellow_line.width(2)
    xcor = 1000
    ycor = -300
    yl_xcor = 300
    
    while ycor < 300:
        Road.penup()
        Road.goto(xcor,ycor)
        Road.pendown()
        Road.setpos(-xcor,ycor)
        ycor += 25
        print(ycor)
        if ycor < 250 :
            Yellow_line.penup()
            Yellow_line.setpos(xcor,ycor)
            Yellow_line.pendown()
            Yellow_line.setpos(-xcor,ycor)
        ycor +=25
        print(ycor)
        time.sleep(0.1)
        screen.update()
    FinishLine = Turtle()
    FinishLine.width(10)
    FinishLine.teleport(xcor,310)
    FinishLine.setheading(180)
    FinishLine.shape('square')
    while FinishLine.xcor() > -1000:
        FinishLine.color('white')
        FinishLine.forward(30)
        FinishLine.color("black")
        FinishLine.forward(30)
    screen.update()
draw_board()

player = Player()
car_man = CarManager(30)
screen.listen()
screen.onkeypress(key="Up",fun=player.Move_up)
screen.onkeypress(key="Down",fun=player.Move_down)
screen.onkeypress(key="Left",fun=player.Move_left)
screen.onkeypress(key="Right",fun=player.Move_right)

game_is_on = True
while game_is_on:
    screen.update()
    car_man.Car_move(player.position())
    if car_man.collision:
        player.reset()
        player.scoreboard.Display_Gameover()
        game_is_on = False
        car_man.collision = False
    if player.positiony() > 310:
        player.Level_clear()
        car_man.speed += car_manager.MOVE_INCREMENT
    screen.update()
    time.sleep(0.01)
    
screen.exitonclick()