#Assignment 4.5
#Make a list of the numbers from one to one million
#Then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1,1000001))
print(f"min value is {min(numbers)}")
print(f"max value is {max(numbers)}")
print(f"sum of 1 million numbers is {sum(numbers)}")