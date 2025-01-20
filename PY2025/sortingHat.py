# Hogwarts Sorting Hat Algorithm - www.101computing.net/hogwarts-sorting-hat-algorithm
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

q1 = input("Are you brave? ")
q2 = input("Are you patient? ")
q3 = input("Are you focused? ")
q4 = input("Are you creative? ")
q5 = input("Are you organised? ")
q6 = input("Are you kind? ")
q7 = input("Do you play fair? ")
q8 = input("Are you loyal? ")
q9 = input("Are you competitive? ")
q10 = input("Do you have strong friendship values? ")

if q1 == "yes":
    G += 1
    if q2 == "yes":
        H += 1
    elif q2 == "no":
        S += 1
        if q3 == "yes":
            R += 1
            if q4 == "yes":
                R += 1
                if q5 == "yes":
                    R += 1
                    if q6 == "yes":
                        H += 1
                        R += 1
                        G += 1
                        if q7 == "yes":
                            H += 1
                            G += 1
                        elif q7 == "no":
                            S += 1
                            if q8 == "yes":
                                G += 1
                                R += 1
                            elif q8 == "no":
                                S += 1
                                if q9 == "yes":
                                    G += 1
                                    S += 1
                                    if q10 == "yes":
                                        G += 1
                                        R += 1
                                        H += 1
                                    elif q10 == "no":
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