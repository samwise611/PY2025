print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? £"))
tipAmount = int(input("How much tip would you like to give? 10, 12, or 15? "))
totalPeople = int(input("How many people split the bill? "))

billWithTip = tipAmount / 100 * totalBill + totalBill
#print(billWithTip)

billPerPerson = billWithTip / totalPeople
finalBill = round(billPerPerson, 2)
print(f"Each person owes: £{finalBill}")

