print('---------- Exercises 0 -------------')

from turtle import *

#1 Square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

mainloop()


#2 Square centered on screen

# move into position
up()
forward(50)
left(90)
forward(50)
left(90)

down()

# draw the square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

mainloop()

#3 Orange Circle
pencolor('orange')
width(10)
circle(180)


#4 Star

for i in range(5):
    forward(100)
    right(144)
mainloop()

