print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to treasure island! \nYour mission is to find the treasure.")
path = input("You are at a cross roads (left or right)... ")
if path == str.lower("right"):
    print("you fall in a hole and die")
elif path == str.lower("left"):
    print("you reach the lake")
    lake = input("swim or wait... ")
    if lake == str.lower("swim"):
        print("you drown and die")
    elif lake == str.lower("wait"):
        print("you see 3 doors")
        door = input("red, yellow or blue... ")
        if door == str.lower("yellow"):
            print("you win")
        elif door == str.lower("red"):
            print("your burn and die")
        elif door == str.lower("blue"):
            print("wild dog attacks you die")
        else:
            print("incorrect command")
    else:
        print("incorrect command")

else:
    print("incorrect command")