import random
friends = ["Alice", "Bob", "Charlie", "David", "Sam"]
randomInt = random.randint(1, 5)
if randomInt == 1:
    print("Alice")
elif randomInt == 2:
    print("Bob")
elif randomInt == 3:
    print("Charlie")
elif randomInt == 4:
    print("David")
else:
    print("Sam")

# in 1 line of code
print(random.choice(friends))