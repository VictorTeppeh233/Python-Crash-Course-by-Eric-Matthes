#Accessing a File’s Lines
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

#splitlines() is a string method that splits a string into a list of lines.
lines = contents.splitlines()
for line in lines:
    print(line)