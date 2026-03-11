#Assignment 4.10

# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message.
# The first three items in the list are:.
# Then use a slice to print the first three items from that program’s list.
# Print the message 
# Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.
# Print the message 
# The last three items in the list are:. 
# Then use a slice to print the last three items in the list.

numbers = list(range(3,31,3))
for num in numbers:
    print(num)

print("The first three items in the list are:")
print(numbers[:3])

print("Three items from the middle of the list are")
len_of_num = len(numbers)
half_of_len = len_of_num//2
half_of_len -= 1
print(numbers[half_of_len:half_of_len+3])

print("The last three items in the list are:")
print(numbers[-3:])