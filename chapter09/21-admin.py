# assignment 9.7

"""
An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in 
Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method.

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

#creating the child class
class Admin(User):
    """Creating the child class"""
    def __init__(self, first_name, last_name, email, user_name, login_attempts):
        """Allowing the child class to use the parents methods"""
        super().__init__(first_name, last_name, email, user_name, login_attempts)
        self.priviledges = ["can add user", "can delete user", "can ban user"]

    def show_priviledges(self):
        """Showing the priviledges of Admin"""
        for item in self.priviledges:
            print(f"Admin {item}.")

#instantiate the class
user_1 = Admin('albert', 'einstein', 'aeinstein@gmail.com', 'aeinstein', '3')
#calling a method in the child clas
user_1.show_priviledges()