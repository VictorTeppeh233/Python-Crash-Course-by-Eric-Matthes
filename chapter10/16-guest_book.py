# assignment 10.5

"""
Write a while loop that prompts users for their name. 
Collect all the names that are entered, 
and then write these names to a file called guest_book.txt. 
Make sure each entry appears on a new line in the file.
"""

from pathlib import Path

path = Path("guest_book.txt")

guests = []

while True:
    name = input("Enter your name (or 'quit'): ")

    if name == "quit":
        break

    guests.append(name)

path.write_text("\n".join(guests))