# Retrieving data using json.loads()

#importing the modules
from pathlib import Path
import json

#creating the file path
path = Path('numbers.json')
#reading everything in the file as a string
contents = path.read_text()
#converts JSON string to python object
numbers = json.loads(contents)
#prints the python list
print(numbers)