print("-----Step 1-----")
secret_number = 5
x = int(input("I\'m thinking of a number between 1 and 10. What\'s the number? "))
while x != secret_number:
    x = int(input("Nope, try again. What\'s the number? "))
if x == 5:
    print("Yes, you win!")

print("-----Step 2-----")
secret_number = 5
x = int(input("I\'m thinking of a number between 1 and 10. What\'s the number? "))
while x != secret_number:
  if x > 5:
     x = int(input(str(x) + " is too high. What\'s the number? "))
  if x < 5:
     x = int(input(str(x) + " is too low. What\'s the number? "))
if x == 5:
    print("Yes, you win!")

print("-----Step 3-----")
import random 
my_random_number = random.randint(1, 10)
x = int(input("I\'m thinking of a number between 1 and 10. What\'s the number? "))
while x != my_random_number:
  if my_random_number < x:
     x = int(input(str(x) + " is too high. What\'s the number? "))
  if my_random_number > x:
     x = int(input(str(x) + " is too low. What\'s the number? "))
if x == my_random_number:
    print("Yes, you win!")

print("-----Step 4-----")
import random 
my_random_number = random.randint(1, 10)
x = int(input("I\'m thinking of a number between 1 and 10. You have 5 guesses. What\'s the number? "))
guess_count = 5
while x != my_random_number:
  if guess_count > 1:
    if my_random_number < x:
       guess_count -= 1
       x = int(input(str(x) + " is too high. You have " + str(guess_count) + " guesses left. What\'s the number? "))
    elif my_random_number > x:
       guess_count -= 1
       x = int(input(str(x) + " is too low. You have " + str(guess_count) + " guesses left. What\'s the number? "))
  else:
    if my_random_number < x:
       print((str(x) + " is too high. You ran out of guesses!"))
       break
    if my_random_number > x:
       print((str(x) + " is too low. You ran out of guesses!"))
       break
if x == my_random_number:
    print("Yes, you win!")

print("-----Bonus-----")
import random
replay = 'y'
while replay == 'y': 
  my_random_number = random.randint(1, 10)
  x = int(input("I\'m thinking of a number between 1 and 10. You have 5 guesses. What\'s the number? "))
  guess_count = 5
  while x != my_random_number:
    if guess_count > 1:
      if my_random_number < x:
        guess_count -= 1
        x = int(input(str(x) + " is too high. You have " + str(guess_count) + " guesses left. What\'s the number? "))
      elif my_random_number > x:
        guess_count -= 1
        x = int(input(str(x) + " is too low. You have " + str(guess_count) + " guesses left. What\'s the number? "))
    else:
      if my_random_number < x:
        print((str(x) + " is too high. You ran out of guesses!"))
        break
      if my_random_number > x:
        print((str(x) + " is too low. You ran out of guesses!"))
        break
  if x == my_random_number:
      print("Yes, you win!")
  replay = input('Would you like to play again? ')
print("Bye")