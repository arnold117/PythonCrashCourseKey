"""
You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.

•	Start with your program from Exercise 3-4 or Exercise 3-5.
Add a print statement to the end of your program informing people that you found a bigger dinner table.

•	Use insert() to add one new guest to the beginning of your list.

•	Use insert() to add one new guest to the middle of your list.

•	Use append() to add one new guest to the end of your list.

Print a new set of invitation messages, one for each person in your list.
"""

guests = ['james van jan', 'alice von bock', 'apollo la burch']

for name in guests:
    msg = "Dear " + name.title() + ", please come to dinner!"
    print(msg)

msg = "\nSorry, " + guests[1].title() + " cannot make it to dinner.\n"
print(msg)

del(guests[1])
guests.insert(1, 'gary snyder')

for name in guests:
    msg = "Dear " + name.title() + ", please come to dinner!"
    print(msg)

msg = "\n* Found a bigger Table: *Exist.\n"
print(msg)

guests.insert(0, 'guido van rossum')
guests.insert(2, 'jack turner')
guests.append('lynn hill')

for name in guests:
    msg = "Dear " + name.title() + ", please come to dinner!"
    print(msg)
