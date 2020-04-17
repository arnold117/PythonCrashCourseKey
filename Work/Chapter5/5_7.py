"""
Make a list of your favorite fruits,
and then write a series of independent if statements that check for certain fruits in your list.
•	Make a list of your three favorite fruits and call it favorite_fruits.
•	Write five if statements. Each should check whether a certain kind of fruit is in your list.
 If the fruit is in your list, the if block should print a statement, such as You really like bananas!
"""

favourite_fruits = ['banana', 'apple', 'peach']
fruits = ['blueberry', 'blackberry', 'strawberry', 'berry', 'peach']

for fruit in fruits:
    if fruit in favourite_fruits:
        msg = "Wow, you really love " + fruit + "!"
        print(msg)
