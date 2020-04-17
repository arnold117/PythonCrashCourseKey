"""
Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

people = []

person = {
    'first_name': 'arnold',
    'last_name': 'Chow',
    'age': 18,
    'city': 'beijing',
}

people.append(person)

person = {
    'first_name': 'alice',
    'last_name': 'von bock',
    'age': 18,
    'city': 'berlin',
}

people.append(person)

person = {
    'first_name': 'taiga',
    'last_name': 'aisaka',
    'age': 16,
    'city': 'tokyo',
}

people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    msg = name + ", of " + city + " is " + age + " years old."
    print(msg)
