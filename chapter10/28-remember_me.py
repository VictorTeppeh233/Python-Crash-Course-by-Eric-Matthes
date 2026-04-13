# Refactoring
# Importing modules
from pathlib import Path
import json

# This function tries to get the username from the file
def get_stored_username(path):
    """Get stored username if available."""
    
    # Check if the file exists
    if path.exists():
        # Read the file content as text
        contents = path.read_text()
        
        # Convert JSON string back to Python data (username)
        username = json.loads(contents)
        
        # Return the username
        return username
    else:
        # If file doesn't exist, return None
        return None
    

# This function asks the user for a new username and saves it
def get_new_username(path):
    """Prompt for a new username."""
    
    # Ask user to input their name
    username = input("What is your name? ")
    
    # Convert the username into JSON format (string)
    contents = json.dumps(username)
    
    # Save it to the file
    path.write_text(contents)
    
    # Return the username
    return username


# This function controls the program
def greet_user():
    """Greet the user by name."""
    
    # Create a path to the file where username is stored
    path = Path('username.json')
    
    # Try to get an existing username
    username = get_stored_username(path)
    
    # If a username was found
    if username:
        # Welcome the user back
        print(f"Welcome back, {username}!")
    else:
        # If no username, ask for a new one
        username = get_new_username(path)
        
        # Tell user their name will be remembered
        print(f"We'll remember you when you come back, {username}!")
    

# Run the program
greet_user()