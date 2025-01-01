from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(position)



screen.exitonclick()