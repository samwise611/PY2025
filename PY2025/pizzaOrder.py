print("Welcome to the pizza shop.")
size = input("What size pizza do you want S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("incorrect input")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extraCheese == "Y":
    bill += 1

print(f"Your bill is: £{bill}")