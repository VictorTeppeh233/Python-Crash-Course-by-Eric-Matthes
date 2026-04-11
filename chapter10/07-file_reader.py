#Working with a File’s Contents
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    #removes the white space on the left side of the digits
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))