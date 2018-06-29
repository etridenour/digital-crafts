from turtle import *

def eq_triangle(x, y, z, f):
    color(y)
    width(z)
    if f == True:
        begin_fill()
        forward(x)
        left(120)
        forward(x)
        left(120)
        forward(x)
        end_fill()
    else:
        forward(x)
        left(120)
        forward(x)
        left(120)
        forward(x)
    
def square(x, y, z, f):
    color(y)
    width(z)
    if f == True:
        begin_fill()
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)
        end_fill()
    else:
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)
        left(90)
        forward(x)

def pentagon(x, y, z, f):
    color(y)
    width(z)
    if f == True:
        begin_fill()
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        end_fill()
    else:
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        left(72)
        forward(x)
        

def hexagon(x, y, z, f):
    color(y)
    width(z)
    if f == True:
        begin_fill()
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        end_fill()
    else:
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)
        left(60)
        forward(x)

def octagon(x, y, z, f):
    color(y)
    width(z)
    if f == True:
        begin_fill()
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        end_fill()
    else:
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)
        left(45)
        forward(x)


def star(x, y, z, f):
    color(y)
    if f == True:
        begin_fill()
        for i in range(5):
            forward(x)
            right(144)
        end_fill()
    else:
        for i in range(5):
            forward(x)
            right(144)

def cir(x, y, z, f):
    if f == True:
        begin_fill()
        color(y)
        width(z)
        circle(x)
        end_fill()
    else:
        color(y)
        width(z)
        circle(x)


