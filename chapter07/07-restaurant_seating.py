# Assignment 7.2

"""
Write a program that asks the user how many people are in their dinner group. 
If the answer is more than eight, 
print a message saying they’ll have to wait for a table. Otherwise, 
report that their table is ready.
"""
message = "Welcome, please how many people are in you dinner group? \n"

waiter = input(message)
waiter = int(waiter)

if waiter > 8:
    print("They'll have to wait for a table.")
else:
    print("The table is ready.")