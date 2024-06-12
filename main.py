import turtle as t
from turtle import Screen
import random

line = t.Turtle()
t.colormode(255)
line.speed("fastest")


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    size = (r, g, b)
    return size


for _ in range(100):
    line.color(random_color())
    line.circle(100)
    line.left(10)


screen = Screen()
screen.exitonclick()
