import turtle

t = turtle.Turtle()

def drawsquare(t, x):
    t.pendown()
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)

def squares(t, y):
    i = 1
    while i <= y:
        drawsquare(t, 100)
        t.left(360)
        i += 1
