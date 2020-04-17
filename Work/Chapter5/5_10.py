"""
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
•	Make a list of five or more username called current_users.
Make another list of five username called new_users.
Make sure one or two of the new username are also in the current_users list.
•	Loop through the new_users list to see if each new username has already been used.
If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
•	Make sure your comparison is case insensitive.
If 'John' has been used, 'JOHN' should not be accepted.
"""

current_users = ['Eric', 'Admin', 'alice', 'peTer', 'swine', 'Noa']
new_users = ['Adam', 'Django', 'Java', 'noa', 'alice']

current_users_lower = [user.lower() for user in current_users]

'''
This is another way:
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
'''

for user in new_users:
    if user.lower() in current_users_lower:
        msg = "Sorry, " + user + " was taken!"
    else:
        msg = "Great, " + user + " is available!"
    print(msg)
