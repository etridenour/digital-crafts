print('-----Number 1-----')
for x in range(1, 11):
    print(x)

print('-----Number 2-----')
x = int(input("Starting number: "))
y = int(input("Ending number: ")) + 1
for num in range(x, y):
    print(num)

print('-----Number 3-----')
for x in range(1, 10):
    if x % 2 != 0:
        print(x)

print('-----Number 4-----')
star = "*"
for x in range(0, 5):
    print(star * 5)

print('-----Number 5-----')
square = int(input("How big is the square?: "))
star = '*'
for x in range(0, square):
    print(star * square)

print('-----Number 6-----')
x = int(input("Width?: "))
y = int(input("Height?: "))
star = '*'
for c in range(0, y):
    print(star * x)

print('-----Number 7-----')
star = '*' 
for i in range(1,8,2):
    print(star * i)

print('-----Number 8-----')
height = int(input("What is the height? "))
star = '*' 
for i in range(height):
    print((star*i).rjust(height-1) + star + (star*i).ljust(height-1))

print('-----Number 9-----')
for x in range(1, 11): 
    for j in range(1, 11): 
        n = j * x
        print( "{} x {} = {}".format(x, j, n))



