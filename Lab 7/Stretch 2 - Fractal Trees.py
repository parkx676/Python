## Fractal Trees

import turtle
import random

t = turtle.Turtle()
t.left(90)
def tree(t, trunkLength):
    angle = random.randint(15, 45)
    length = random.randint(12, 18)
    if trunkLength < 5:
        return
    else:
        t.forward(trunkLength)
        t.right(angle)
        tree(t, trunkLength-length)
        t.left(angle * 2)
        tree(t, trunkLength-length)
        t.right(angle)
        t.backward(trunkLength)
