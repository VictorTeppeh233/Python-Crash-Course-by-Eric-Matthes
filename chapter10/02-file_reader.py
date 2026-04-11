# Reading the Contents of a File
# This imports the Path class from Python’s built-in pathlib module.
from pathlib import Path

#This creates a Path object that points to a file named pi_digits.txt.
path = Path('pi_digits.txt')

#This reads the entire content of the file as a string. 
#Everything inside pi_digits.txt (text, numbers, line breaks) is stored in the variable contents.
#Then assigns it to varible "contents"
contents = path.read_text()

#rstrip() is a string method in Python.
#It removes whitespace from the right (end) of a string.
contents = contents.rstrip()

#This simply prints whatever was read from the file to the screen.
print(contents)