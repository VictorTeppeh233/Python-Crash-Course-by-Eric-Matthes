# Passing Arguments
# Default Values

#defining the function
#the default value for animal_type is dog
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#calling the function
describe_pet(pet_name="jack")
describe_pet('milo')
describe_pet('missy', 'cat')