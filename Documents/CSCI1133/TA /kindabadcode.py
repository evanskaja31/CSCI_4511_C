import turtle
import random

def drawsquare(size):
    turtle.color((random.random(), random.random(), random.random()))
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

turtle.speed(6)
drawsquare(125)
drawsquare(100)
drawsquare(75)
drawsquare(50)
drawsquare(25)
