"""
Add an if test to hello_admin.py to make sure the list of users is not empty.
•	If the list is emtpy, print the message We need to find some users!
•	Remove all of the username from your list, and make sure the correct message is printed.
"""

username = []

if username:
    for user in username:
        if user == 'admin':
            msg = "Hello Admin, would you like to see a status report?"
        else:
            msg = "Hello " + user + ", thank you for log in again!"
        print(msg)
else:
    print("No username found!")
