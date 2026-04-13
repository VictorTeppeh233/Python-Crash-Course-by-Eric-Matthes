# Storing data using json.dumps()
#importing modules
from pathlib import Path
import json

#creating a list of numbers
numbers = [2, 3, 5, 7, 11, 13]

#creating the file path
path = Path('numbers.json')

#converts python data to JSON string
contents = json.dumps(numbers)

#writes the JSON string into numbers.json
path.write_text(contents)