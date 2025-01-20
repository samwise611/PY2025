#Ice Cream Price Calculator - www.101computing.net/ice-cream-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+      The Ice Cream Shop       +")
print("+            Welcome            +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

container = input("What type of ice cream container would you like: cup or cone?\n")
while container!="cup" and container!="cone":
   print("Invalid answer please try again!")
   container = input("What type of ice cream container would you like: cup or cone?")

scoopNum = int(input("How many scoops would you like? (1 - 4)\n"))
addFlake = input("Would you like a Flake? (Y/N)\n")
addSprinkle = input("Would you like Sprinkles? (Y/N)\n")
addStrawberry = input("Would you like Strawberry Sauce? (Y/N)\n")

price = 0.00
cup = 0.50
cone = 0.80
scoop = 1.00 * scoopNum
flake = 0.40
sprinkles = 0.30
strawberrySauce = 0.60

if container == "cup":
    price += cup
elif container == "cone":
    price += cone
    if 4 <= scoop >= 1:
        price += scoop
    else:
        print("invalid number")
        if addFlake == "Y":
            price += flake
            if addSprinkle == "Y":
                price += sprinkles
                if addStrawberry == "Y":
                    price += strawberrySauce

# incorrect not adding full price.