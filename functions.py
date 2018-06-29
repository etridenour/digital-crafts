print('---------- 1.Hello -------------')

def hello(name):
    return "Hello " + name
print(hello("Veronica"))


print('---------- 2. y = x + 1 -------------')

import matplotlib.pyplot as plot 

def f(x): 
     return x + 1

xs = list(range(-3, 4)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()


print('---------- 3. Square of x -------------')

def f(x): 
     return x ** 2

xs = list(range(-100, 100, 1)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()

print('---------- 4. Odd or Even -------------')

def f(x): 
     if x % 2 != 0:
         return 1
     else:
         return -1

xs = list(range(-5, 5, 1)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.bar(xs, ys) 
plot.show()

print('---------- 5. Sine -------------')

import math

def f(x): 
     return math.sin(x)

xs = list(range(-5, 5, 1)) 
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()

print('---------- 6. Sine 2 -------------')

from numpy import arange

def f(x): 
     return math.sin(x)

xs = list(arange(-5, 5, 0.1))
ys = [] 

for x in xs: 
     ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()

print('---------- 7.Degree Conversion -------------')

def tempF(x):
    return x * float(1.8) + 32

xs = float(tempF(32))
ys = 0 

plot.plot(xs, ys, 'g^:')
plot.show()

print('---------- 8.Play again? -------------')

def playAgain():
    x = input("Do you want to play again (Y or N)? ")
    if x == 'Y':
        return True
    else:
        return False

print(playAgain())


print('---------- 8.Play again? Again? -------------')

def playAgain():
    x = input("Do you want to play again (Y or N)? ")
    if x == 'Y':
        return True
    elif x == "N":
        return False
    else:
        print("Invalid Input")
        playAgain()

playAgain()
