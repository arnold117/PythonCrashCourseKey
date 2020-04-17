"""
If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.
"""
guests = ['james van jan', 'alice von bock', 'apollo la burch']

for name in guests:
    msg = "Dear " + name.title() + ", please come to dinner !"
    print(msg)
