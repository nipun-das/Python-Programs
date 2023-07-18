import turtle

t = turtle.Turtle()

def square(t, length):
    t.fillcolor("orange")
    t.begin_fill()

    for count in range(4):
        t.forward(length)
        t.left(90)

    t.end_fill()

square(t, 100)
