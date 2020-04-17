"""
You just heard that one of your guests can’t make the dinner,
 so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.

Start with your program from Exercise 3-4.
Add a print statement at the end of your program stating the name of the guest who can’t make it.

Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

Print a second set of invitation messages, one for each person who is still in your list.
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