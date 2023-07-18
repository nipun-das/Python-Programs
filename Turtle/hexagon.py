import turtle

t = turtle.Turtle()


def hexagon(t, length):
    for i in range(6):
        t.forward(length)
        t.left(60)


hexagon(t, 30)
