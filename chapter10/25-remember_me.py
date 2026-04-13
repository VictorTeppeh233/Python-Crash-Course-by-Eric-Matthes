#Saving and Reading User-Generated Data
#importing modules
from pathlib import Path
import json

#variable to store the username
username = input("What is your name? ")
#creating the file path object
path =Path('username.json')
#It converts username into a JSON-formatted string and stores it in contents.
contents = json.dumps(username)
#writes the vlaue of contents into the file
path.write_text(contents)
#Prints the message along with username
print(f"We'll remember you when you come back, {username}!")
