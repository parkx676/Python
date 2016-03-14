## Stretch
import turtle
import random

myt = circle.draw()
scr = turtle.Screen()
scr.delay(0)
myt.speed(0)
myt.hideturtle()
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

def randColor():
    idx = random.randint(0, 5)
    return colors[idx]

class shape():
    def __init__(self, x=0, y=0, istr = "", ibool = False):
        self.__xloc = x
        self.__yloc = y
        self.__Fillcolor = istr
        self.__Filled = ibool
        
    def setFillcolor(self, istr):
        self.__Fillcolor = istr

    def setFilled(self, ibool):
        self.__Filled = ibool

    def isFilled(self):
        return str(self.__Filled)


class circle(shape):
    def __init__(self, x=0, y=0, r=1):
        super().__init__()
        self.__radius = r

    def draw(turtle):
        super().setFilled(randColor)
        turtle.penup()
        turtle.goto(super().__init__(x, y))
        turtle.pendown()
        if turtle.isFilled(self) == 'True':
            turtle.fillcolor(super().setFillcolor())
            turtle.begin_fill()
            turtle.circle(self.__radius)
            turtle.end_fill()
        else:
            turtle.circle(self.__radius)


        
