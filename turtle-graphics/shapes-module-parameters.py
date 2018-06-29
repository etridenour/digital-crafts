from turtle import *
import shapesP

up()
left(90)
forward(225)
left(90)
forward(350)
right(180)
down()

shapesP.eq_triangle(75, 'red', 1, True)

up()
left(120)
forward(275)
down()

shapesP.square(150, 'yellow', 10, True)

up()
left(90)
forward(275)
down()

shapesP.pentagon(40, 'green', 20, False)

up()
right(18)
forward(150)
right(90)
down()

shapesP.hexagon(100, 'purple', 2, True)

up()
left(60)
forward(360)
down()

shapesP.octagon(80, 'pink', 10, False)

up()
left(45)
forward(60)
left(90)
forward(250)
left(18)
down()

shapesP.star(50, 'orange', 3, True)

up()
left(50)
forward(400)
down()

shapesP.cir(200, 'blue', 7, False)

mainloop()

