#4
print("-----Problem #4-----")
day = int(input('Day (0-6)? '))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days[day])

#5
print("-----Problem #5-----")
day = int(input('Day (0-6)? '))
if 5 >= day >= 1:
    print("Go to Work!")
elif day == 0 or day == 6:
    print("Sleep in")    

#6
print("-----Problem #6-----")
tempC = input("What is the temperature in Celcius?: ")
def tempF(x):
    temp = float(x) * 1.8 + 32
    return str(temp) + " F"

print(tempF(tempC))

#7
print("-----Problem #7-----")
bill = float(input("What is the total bill amount?: $"))
service = input("What was the level of service: good, fair or bad?: ")

if service == "good":
    tip = float(bill) * 0.2
elif service == "fair":
    tip = float(bill) * 0.15
elif service == "bad":
    tip = float(bill) * 0.1

print("Tip amount: " + "{:.2f}".format(tip))
print("Total amount: " + "{:.2f}".format(tip + bill))

#8
print("-----Problem #8-----")
bill = float(input("What is the total bill amount?: $"))
service = input("What was the level of service: good, fair or bad?: ")
split = int(input("Split how many ways? "))

if service == "good":
    tip = float(bill) * 0.2
elif service == "fair":
    tip = float(bill) * 0.15
elif service == "bad":
    tip = float(bill) * 0.1

check_split = float("{:.2f}".format(tip + bill)) / split

print("Tip amount: " + "{:.2f}".format(tip))
print("Total amount: " + "{:.2f}".format(tip + bill))
print("Amount per person: " + "{:.2f}".format(check_split))


#9
print("-----Problem #9-----")
for number in range(0, 11):
    print(number)

#10
print("-----Problem #10-----")
coin = 0
x = input("You have " + str(coin) + " coins. Would you like another? ")
while x == 'yes':
  coin += 1
  x = input("You have " + str(coin) + " coins. Would you like another? ")
if x == "no":
  print("Bye")

    



