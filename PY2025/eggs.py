# https://www.101computing.net/the-egg-farmer-puzzle/

eggs = int(input("how many eggs? "))
eggs12 = int(eggs / 12)
eggs6 = (eggs % 12)
bfast = eggs6 - 6

if eggs >= 100 or eggs <= 150:
    print(f"You need {eggs12} cartons of 12")
    if eggs6 >= 6:
        newEgg6 = int(eggs12 / 6)
        print(f"You need {newEgg6} cartons of 6")
        print(f"You have {bfast} eggs for breakfast")
    elif 0 < eggs6 < 6:
        print(f"You have {eggs6} eggs for breakfast")
