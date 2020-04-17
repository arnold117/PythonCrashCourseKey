"""
Write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they’ll have to wait for a table.
Otherwise, report that their table is ready.
"""

num = input("How many people do you have?")

if int(num) > 8:
    msg = "Sorry, you have to wait for a moment."
else:
    msg = "There is a table ready for you."

print(msg)
