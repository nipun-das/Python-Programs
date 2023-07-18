import turtle

t= turtle.Turtle()

def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)
square(t,30)