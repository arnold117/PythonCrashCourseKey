"""
Make a list of five or more username, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user:
•	If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
•	Otherwise, print a generic greeting, such as Hello Eric, thank you for log in in again.
"""

username = ['eric', 'admin', 'alice', 'peter', 'swine', 'noa']

for user in username:
    if user == 'admin':
        msg = "Hello Admin, would you like to see a status report?"
    else:
        msg = "Hello " + user + ", thank you for log in again!"
    print(msg)
