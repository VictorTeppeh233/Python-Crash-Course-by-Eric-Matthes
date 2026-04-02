# Assignment 7.9

"""
Using the list sandwich_orders, 
make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying 
the deli has run out of pastrami, 
and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

#Making the list of sandwiches
sandwich_orders = ['pastrami sandwich','ham sandwich', 'turkey sandwich','pastrami sandwich', 'grilled cheese sandwich', 'roast beef sandwich','grilled chicked sandwich','pastrami sandwich']
#Made the empty list
finished_sandwiches = []

message = "Unfortuantely we don't have any pastrami sandwich"
print(message)

#usng a while loop to remove pastrami sandwich from the list.
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

#Looping through the sandwich orders and printing the message.
while sandwich_orders:
    #removing the order from the order list.
    sandwiches = sandwich_orders.pop()
    print(f"I am made your {sandwiches}.")
    #adding the order to the new finished list..
    finished_sandwiches.append(sandwiches)
  
    
print('-' * 30)
#printing the sandwiches made
print("I have made these sandwiches.")

#loopng through the list of finished sandwiches and printing them.
for sandwich_made in finished_sandwiches:
    print(f"\t{sandwich_made}")