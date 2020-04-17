"""
Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians
by adding the phrase the Great to each magician’s name.
Call show_magicians() to see that the list has actually been modified.
"""


def show_magicians(magicians):
    """ Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great magicians.
    great_magicians = []

    # make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
