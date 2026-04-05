# Creating and Using a Class

# Define a class named Dog
class Dog:
    """A simple attempt to model a dog."""  # Class docstring describing what the class does

    # The constructor method runs when we create a new Dog object
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name  # Store the dog's name in the object
        self.age = age    # Store the dog's age in the object

    # Method to simulate the dog sitting
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")  # Print a message including the dog's name

    # Method to simulate the dog rolling over
    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")  # Print a message including the dog's name

# Create an instance (object) of the Dog class
my_dog = Dog('Willie', 6)  # 'Willie' is the name, 6 is the age

# Access and print the dog's attributes using dot notation
print(f"My dog's name is {my_dog.name}.")  # Prints: My dog's name is Willie.
print(f"My dog is {my_dog.age} years old.")  # Prints: My dog is 6 years old.