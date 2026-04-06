# assignment 9.3

"""
Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.
"""

#creating the class
class User:
    """Stores details of the User"""
    def __init__(self, first_name, last_name, email, user_name, ):
        """Initialize the first name and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"first name: {self.first_name.title()}")
        print(f"last_name: {self.last_name.title()}")
        print(f"email: {self.email}")
        print(f"user_name: {self.user_name}")
    
    def greet_user(self):
        """Print personalized greeting to the user"""
        print(f"Welcome {self.first_name.title()}, we are glad to have you join us.")

#calling the function
user_1 = User("albert", "einstein", "ealbert@gmail.com", "e_albert")
user_2 = User("john", "doe", "jdoe@gmail.com", "jdoe")

#printing the information of the users
user_1.describe_user()
user_1.greet_user()
print('-' * 30)
user_2.describe_user()
user_2.greet_user()