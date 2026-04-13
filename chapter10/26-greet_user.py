#Saving and Reading User-Generated Data
#importing modules
from pathlib import Path
import json

#creating the file path object
path = Path('username.json')

#reads the json format and stores in contents
contents = path.read_text()

#converts the json format in contents to python and stores it in username
username = json.loads(contents)
#Prints the message along with username
print(f"Welcome back, {username}!")
