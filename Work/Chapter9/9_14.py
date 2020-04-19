from random import randint


class Dice():
    """Represent a dice, which can be rolled."""


    def __init__(self, sides = 6):
        """Initialize the dice."""
        self.sides = sides
    

    def roll_dice(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6-sided dice, and show the results of 10 rolls.
d6 = Dice()

results = []

for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)

print("10 rolls of a 6-sided dice: ")
print(results)

# Make a 10-sided dice, and show the results of 10 rolls.
d10 = Dice(sides=10)

results = []

for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)

print("\n10 rolls of a 10-sided dice: ")
print(results)

# Make a 20-sided dice, and show the results of 10 rolls.
d20 = Dice(sides=20)

results = []

for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)

print("10 rolls of a 20-sided dice: ")
print(results)