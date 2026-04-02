# Passing Arguments
# Keyword Arguments

#defining the function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#calling the function
describe_pet(animal_type='dog', pet_name='jack')