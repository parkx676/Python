## Workout

import turtle
import random

colors = ["red", "yellow", "green", "blue", "purple", "orange"]

def randColor():
    idx = random.randint(0,5)
    return colors[idx]

class shape():
    def __init__(self, x=0, y=0, istr="", ibool=False):
        self.xloc = x
        self.yloc = y
        self.Fillcolor = istr
        self.Filled = ibool

    def setFillcolor(self, istr):
        self.Fillcolor = istr

    def setFilled(self, ibool):
        self.Filled = ibool

    def isFilled(self):
        return self.Filled

class circle(shape):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.radius = r

    def draw(self, myt):
        myt.penup()
        myt.goto(self.xloc, self.yloc)
        myt.pendown()
        if self.isFilled():
            myt.fillcolor(self.Fillcolor)
            myt.begin_fill()
            myt.circle(self.radius)
            myt.end_fill()
        else:
            myt.circle(self.radius)

    def isIN(self, x, y):
        if (x - (self.xloc))**2 + (y - (self.yloc+self.radius))**2 <= self.radius**2:
            return True
        else:
            return False

class rectangle(shape):
    def __init__(self, x=0, y=0, w=1, h=1):
        super().__init__(x, y)
        self.width = w
        self.height = h

    def draw(self, myt):
        myt.penup()
        myt.goto(self.xloc, self.yloc)
        myt.pendown()
        if self.isFilled():
            myt.fillcolor(self.Fillcolor)
            myt.begin_fill()
            for i in range(2):
                myt.forward(self.width)
                myt.left(90)
                myt.forward(self.height)
                myt.left(90)
            myt.end_fill()
        else:
            for i in range(2):
                myt.forward(self.width)
                myt.left(90)
                myt.forward(self.height)
                myt.left(90)

    def isIN(self, x, y):
        if (x-(self.xloc + self.width))+ (y-(self.yloc + self.height)) <= (self.width * self.height):
            return True
        else:
            return False
        

class Display():
    def __init__(self, mty=turtle.Turtle(), scr=turtle.Screen()):
        self.element = []
        self.myt = turtle.Turtle()
        self.scr = turtle.Screen()
        self.scr.delay(0)
        self.myt.speed(0)
        self.myt.hideturtle()
        self.scr.onclick(self.mouseEvent)
        self.scr.listen()
        
    def mouseEvent(self, x, y):
        deter = random.randint(1,2)
        if deter == 1:  
            a = circle(x,y,(random.randint(10, 100)))
        elif deter == 2:
            a = rectangle(x,y,(random.randint(10, 100)),(random.randint(10, 100)))
        a.setFillcolor(randColor())
        a.setFilled(True)
        done = False
        for i in self.element:
            if i.isIN(x,y) == True:
                self.remove(i)
                done = True
        if done == False:
            self.add(a)
        self.myt.clear()
        for i in self.element:
            i.draw(self.myt)

    def add(self, x):
        self.element.append(x)
        
    def remove(self, x):
        self.element.remove(x)

dis = Display()
