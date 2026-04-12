# assignment 10.3

from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    #removes the white space on the left side of the digits
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))