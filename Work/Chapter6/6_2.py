"""
Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.
"""

favourite_numbers = {
    'ada': 1,
    'alice': 2,
    'ark': 3,
    'arnold': 4,
    'pip': 5,
    'cpp': 6,
}

for name in favourite_numbers:
    num = favourite_numbers[name]
    msg = name.title() + "\'s favourite number is " + str(num) + "."
    print(msg)
