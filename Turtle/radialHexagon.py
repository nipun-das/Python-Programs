import turtle

t = turtle.Turtle()


def hexagon(t, length):
    for i in range(6):
        t.forward(length)
        t.left(60)


def radialHex(t, n, length):
    for i in range(n):
        hexagon(t, length)
        t.left(360 / n)


radialHex(t, 5, 100)
