"""
Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value.
Call your function for three different cities,
at least one of which is not in the default country.
"""


def describe_city(city,country = 'chile'):
    """Describe a city"""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)


describe_city('santiago')
describe_city('reyjavik', 'iceland')
describe_city('punta arenas')
