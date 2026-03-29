#Assignment 6.3

"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
•Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or 
print the word on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {
    "list": "a collection of ordered, changeable items.",
    "tuple": "an ordered collection of items that are immutable.",
    "iterate": "go through each item in a collection one by one.",
    "dictionary": "collection of key-value pairs.",
    "sort": "arrange items in a particular order.",
    }

for word in glossary:
    print(f'{word}: {glossary[word]}\n')