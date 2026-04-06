# assignment 9.3

"""
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, 
and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""

#creating the class
class User:
    """Stores details of the User"""
    def __init__(self, first_name, last_name, email, user_name, login_attempts):
        """Initialize the first name and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.login_attempts = login_attempts

    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"first name: {self.first_name.title()}")
        print(f"last_name: {self.last_name.title()}")
        print(f"email: {self.email}")
        print(f"user_name: {self.user_name}")
    
    def greet_user(self):
        """Print personalized greeting to the user"""
        print(f"Welcome {self.first_name.title()}, we are glad to have you join us.")

    def increment_login_attempts(self):
        """Increases the login attempts count by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the login attempts count to 0"""
        self.login_attempts = 0

    def print_login_attempts(self):
        """Prints the login attempts"""
        print(self.login_attempts)


#initialize the class
user_1 = User("albert", "einstein", "ealbert@gmail.com", "e_albert", 0)
user_2 = User("john", "doe", "jdoe@gmail.com", "jdoe", 3)

#printing the login attempts
user_1.print_login_attempts()

#increase the attempts by 1
user_1.increment_login_attempts()
#print the login attempts
user_1.print_login_attempts()
#reset the login attempts
user_1.reset_login_attempts()
#print the login attempts
user_1.print_login_attempts()
