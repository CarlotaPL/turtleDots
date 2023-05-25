from turtle import *
import random

#colors_list was set based on the colors extracted from the image.jpg with the use of colorgram.py

colors_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = Turtle()

#setting the initial attributes
timmy.shape('circle')
timmy.color("white")
timmy.penup()
timmy.hideturtle()


timmy_x = -750
timmy_y = -400
timmy.goto(timmy_x, timmy_y)
timmy.speed('fastest')

def draw_circle(no_of_circles):
    for i in range(no_of_circles):

        colormode(255)
        timmy.fillcolor(random.choice(colors_list))
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)






for circle in range (10):
    draw_circle(10)
    timmy_y +=50
    timmy.goto(timmy_x, timmy_y)
    timmy.setheading(0)


screen  = Screen()
screen.exitonclick()