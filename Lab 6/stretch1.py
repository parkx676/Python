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

i = 1
while i <= 10:
    drawsquare(t, 100)
    t.left(36)
    i += 1
