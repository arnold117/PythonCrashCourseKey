"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""
prompt = "\nWhat topping would you like in your pizza?"
prompt += "\nEnter quit when you are finished:"

while 1:
    topping = input(prompt)
    if topping == "quit":
        break
    msg = "I'll add " + topping + "to your pizza."
    print(msg)
