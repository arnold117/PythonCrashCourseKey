"""
You just found out that your new dinner table won’t arrive in time for the dinner,
and you have space for only two guests.

•	Start with your program from Exercise 3-6.
Add a new line that prints a message saying that you can invite only two people for dinner.

•	Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list,
print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•	Print a message to each of the two people still on your list,
letting them know they’re still invited.

•	Use del to remove the last two names from your list,
so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
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

msg = "\n* Only a small table, no bigger one: *Exist" \
      "Looks like we have to shrink our guest list!\n"
print(msg)

for num in range(5, 1, -1):
    name = guests.pop()
    msg = "Sorry " + name + ", there is no room at the table!"
    print(msg)

for num in range(0, 2, 1):
    msg = "Dear " + guests[num].title() + ", please come to dinner!"
    print(msg)

for num in range(0, 2, 1):
    del(guests[0])

print(guests)
