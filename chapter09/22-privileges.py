# assignment 9.8

"""
Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
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

class Privileges:
    """This is for the privileges of users."""
    def __init__(self):
        self.privileges = ["can add user", "can delete user", "can ban user"]
    """This shows the privileges of an admin"""
    def show_privileges(self):
        """Showing the privileges of Admin"""
        for item in self.privileges:
            print(f"Admin {item}.")


#creating the child class
class Admin(User):
    """Creating the child class"""
    def __init__(self, first_name, last_name, email, user_name, login_attempts):
        """Allowing the child class to use the parents methods"""
        super().__init__(first_name, last_name, email, user_name, login_attempts)
        self.privileges = Privileges()

#instantiate the class
user_1 = Admin('albert', 'einstein', 'aeinstein@gmail.com', 'aeinstein', '3')
#calling a method in the child clas
user_1.privileges.show_privileges()