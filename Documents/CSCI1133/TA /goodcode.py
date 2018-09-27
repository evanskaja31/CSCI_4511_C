import random
import turtle

def drawsquare(size):
    turtle.color((random.random(), random.random(), random.random()))
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def squares(startingsize, numberofsquares):
    currentsize = startingsize
    count = 0
    while count < numberofsquares:
        drawsquare(currentsize)
        count += 1
        currentsize -= (startingsize/numberofsquares)

def main():
    turtle.speed(6)
    usernumberofsquares = turtle.numinput("Number", "Enter a number of squares:")
    userstartingsize = turtle.numinput("Size", "Enter a starting size: ")
    squares(userstartingsize, usernumberofsquares)

if __name__ == "__main__":
    main()
