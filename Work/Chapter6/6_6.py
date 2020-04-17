"""
Use the code in favorite_languages.py (page 104).
•	Make a list of people who should take the favorite languages poll.
Include some names that are already in the dictionary and some that are not.
•	Loop through the list of people who should take the poll.
If they have already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take the poll.
"""

favourite_languages = {
    'arnold': 'c',
    'alice': 'cpp',
    'phil': 'c_sharp',
    'edward': 'java',
    'hug': 'python',
}

for name, language in favourite_languages.items():
    msg = name.title() + "\'s favourite languages is " + language.title() + ". "
    print(msg)

print("\n")

coders = ['arnold', 'alice', 'phil', 'edward', 'neo', 'hug', 'jabber', 'dan']

for coder in coders:
    if coder in favourite_languages.keys():
        msg = "Thank you for taking the poll, " + coder.title() + "!"
    else:
        msg = coder.title() + ", what\'s your favourite language?"

    print(msg)
