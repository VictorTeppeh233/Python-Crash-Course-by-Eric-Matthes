# Using a Function with a while Loop
#defining the function
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#while loop to ask for names then display
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at anytime to quit)")
    #introduced an if statement to quid the loop
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    #formatting the name with the function
    formatted_name = get_formatted_name(f_name, l_name)
    #printing the name
    print(f"\nHello, {formatted_name}")