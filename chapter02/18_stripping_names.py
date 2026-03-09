#Use a variable to represent a person’s name,
#and include some whitespace characters at the beginning and end of the name


name = "\t\n Ada Lovelace \n\t"

# Print with whitespace
print("Original:")
print(name)

# Remove whitespace from the left
print("\nUsing lstrip():")
print(name.lstrip())

# Remove whitespace from the right
print("\nUsing rstrip():")
print(name.rstrip())

# Remove whitespace from both sides
print("\nUsing strip():")
print(name.strip())