"""
A movie theater charges different ticket prices depending on a person’s age.
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tel them the cost of their movie ticket.
"""
prompt = "\nHow old are you?"
prompt += "\nEnter quit when you are finished: "

while 1:
    year = input(prompt)

    if year == "quit":
        break

    if int(year) < 3:
        msg = "You are free of charge!"
    elif int(year) < 12:
        msg = "Your entrance fee is $10!"
    else:
        msg = "Your entrance fee is $15!"

    print(msg)
