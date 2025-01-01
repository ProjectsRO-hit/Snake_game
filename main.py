from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
for position in starting_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(position)
    snake_segments.append(segment)



screen.exitonclick()