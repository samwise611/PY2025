# long conditions streamline

import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
index = [rock, paper, scissors]
player = int(input("type 0 for rock, 1 for paper or 2 for scissors.\n"))
playerChoice = index.pop(player)
print(player, playerChoice)

computerChoice = random.choice(index)
print(f"Computer: {computerChoice}")

if computerChoice == rock and playerChoice == paper:
    print("You win")
elif computerChoice == paper and playerChoice == scissors:
    print("You win")
elif computerChoice == scissors and playerChoice == rock:
    print("You win")

elif computerChoice == rock and playerChoice == scissors:
    print("You loose")
elif computerChoice == paper and playerChoice == rock:
    print("You loose")
elif computerChoice == scissors and playerChoice == paper:
    print("You loose")

elif computerChoice and playerChoice == rock:
    print("Draw")
elif computerChoice and playerChoice == paper:
    print("Draw")
elif computerChoice and playerChoice == scissors:
    print("Draw")

