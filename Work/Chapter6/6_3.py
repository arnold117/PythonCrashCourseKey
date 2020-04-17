"""
•	Think of five programming words you’ve learned about in the previous chapters.
Use these words as the keys in your glossary, and store their meanings as values.
•	Print each word and its meaning as neatly formatted output.
You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented on a second line.
Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.
"""
glossaries = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time',
    'dictionary': 'A collection of key-value pairs',
}

for word in glossaries:
    msg = "\n" + word.title() + ": " + glossaries[word]
    print(msg)
