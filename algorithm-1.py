#1

for x in range(1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
    elif x % 5 == 0:
            print("Buzz")
    elif x % 3 == 0:
            print("Fizz")
    else:
        print(x)

#2

sum = 0
for x in range(1, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum += x

print(sum)

#3
 num1 = 1
 num2 = 2

 numswitch = False
 sum = 0
 array1[1, 2]

 while (num1 < 4000000) and (num2 < 4000000):
     if not numswitch:
         num1  += num2
         array1.append(num1)
         numswitch = True

        else: num2 += num1

#4

num = 600851475143
factors = []
i = 2

while i <= num:
    if num % i ==0:
        factors.append(i)
        num /= i
    i += 1

print(factors)
print(max(factors))



#5
primes = []
num = 2

while len(primes) < 10001;
    factor = 2
    while factor < num:
        if num % factor == 0:
            break
        factor += 1
    if factor == num:
        primes.append(num)
    num += 1

print(primes[len(primes) - 1])
