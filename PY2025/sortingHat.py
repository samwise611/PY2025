# Hogwarts Sorting Hat Algorithm - www.101computing.net/hogwarts-sorting-hat-algorithm
# Needs fix currently cumilating all top scores no mater answer 15Jan

print('''
When a new student join Hogwarts school, 
they are assigned to one of the four school houses depending on their personal qualities. 
The four houses are:

Gryffindor values bravery, loyalty and chivalry
Ravenclaw values curious minds, creativity and inventiveness
Hufflepuff values kindness, friendliness, patience
Slytherin values ambition and competitiveness

Answer yes or no.''')

G = 0
R = 0
H = 0
S = 0

input("Are you brave? ")
if "yes":
    G += 1
input("Are you patient? ")
if "yes":
    H += 1
if "no":
    S += 1
input("Are you focused? ")
if "yes":
    R += 1
input("Are you creative? ")
if "yes":
    R += 1
input("Are you organised? ")
if "yes":
    R += 1
input("Are you kind? ")
if "yes":
    H += 1
    R += 1
    G += 1
input("Do you play fair? ")
if "yes":
    H += 1
    G += 1
if "no":
    S += 1
input("Are you loyal? ")
if "yes":
    G += 1
    R += 1
if "no":
    S += 1
input("Are you competitive? ")
if "yes":
    G += 1
    S += 1
input("Do you value friendship? ")
if "yes":
    G += 1
    R += 1
    H += 1
if "no":
    S += 1
print(f"Ravenclaw: {R} points")
print(f"Hufflepuff: {H} points")
print(f"Gryffindor: {G} points")
print(f"Slytherin: {S} points")

if G >= R and G >= H and G >= S:
    print("You belong to Gryffindor!")
elif R >= G and R >= H and R >= S:
    print("You belong to Ravenclaw!")
elif H >= G and H >= R and H >= S:
    print("You belong to Hufflepuff!")
elif S >= G and S >= H and S >= R:
    print("You belong to Slytherin!")
