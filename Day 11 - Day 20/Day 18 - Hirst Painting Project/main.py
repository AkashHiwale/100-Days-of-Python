from turtle import Turtle, Screen
import random

colors_list = [
    (228, 227, 225), (229, 223, 226), (217, 227, 221), (197, 172, 120),
    (222, 225, 231), (160, 95, 54), (185, 158, 49), (6, 54, 82),
    (126, 35, 22), (56, 29, 24), (121, 164, 179), (111, 69, 85),
    (27, 119, 167), (123, 36, 42), (78, 138, 75), (73, 155, 122),
    (75, 30, 40), (6, 63, 42), (183, 101, 83), (206, 201, 146),
    (140, 176, 161), (175, 152, 158), (177, 202, 188), (22, 81, 59),
    (220, 182, 168)
]

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")

start_x = -225
start_y = -225

timmy.setheading(0)
timmy.setposition(start_x, start_y)

number_of_dots = 10
spacing = 50

def draw_hirst_painting():
    for row in range(number_of_dots):
        for col in range(number_of_dots):
            timmy.dot(30, random.choice(colors_list))
            timmy.forward(spacing)
        timmy.backward(spacing * number_of_dots)
        timmy.sety(timmy.ycor() + spacing)


draw_hirst_painting()
screen.exitonclick()
