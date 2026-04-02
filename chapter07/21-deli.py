# Assignment 7.8

"""
Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. 
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

#Making the list of sandwiches
sandwich_orders = ['ham sandwich', 'turkey sandwich', 'grilled cheese sandwich', 'roast beef sandwich','grilled chicked sandwich']
#Made the empty list
finished_sandwiches = []

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