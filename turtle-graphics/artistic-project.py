from turtle import *
import shapes

speed(50)
def foundation():
    up()
    right(90)
    forward(300)
    left(90)
    down()

    forward(400)
    left(90)
    forward(25)
    left(90)
    forward(800)
    left(90)
    forward(25)
    left(90)
    forward(400)

def door():
    up()
    left(90)
    forward(25)
    right(90)
    forward(20)
    left(90)
    down()

    forward(80)
    left(90)
    forward(40)
    left(90)
    forward(80)

def door_knob():
    up()
    left(180)
    forward(40)
    right(90)
    forward(5)
    down()

    circle(4)

def structure():
    up()
    left(180)
    forward(5)
    left(90)
    forward(40)
    right(90)
    forward(100)
    right(90)
    down()

    forward(400)
    right(90)
    forward (500)
    right (90)
    forward(400)

def roof():
    up()
    left(180)
    forward(400)
    down()

    left(49)
    forward(330)
    left(82)
    forward(330)

def windows():
    up()
    left(49)
    forward(100)
    left(90)
    forward(75)
    down()

    shapes.square(50)

    up()
    left(90)
    forward(100)
    down()

    shapes.square(50)

    up()
    left(90)
    forward(100)
    down()

    shapes.square(50)

    up()
    left(90)
    forward(100)
    down()

    shapes.square(50)

    up()
    forward(75)
    down()

    shapes.square(50)

    up()
    forward(50)
    down()

    shapes.square(50)

    up()
    left(90)
    forward(100)
    down()

    shapes.square(50)

    up()
    left(90)
    forward(100)
    down()

    shapes.square(50)

def garage():
    up()
    left(90)
    forward(130)
    left(90)
    forward(225)
    right(90)
    forward(35)
    right(90)
    down()

    forward(150)
    left(90)
    forward(225)
    left(90)
    forward(150)

    up()
    left(90)
    forward(10)
    left(90)
    down()

    forward(140)
    right(90)
    forward(205)
    right(90)
    forward(140)





foundation()
door()
door_knob()
structure()
roof()
windows()
garage()

mainloop()
