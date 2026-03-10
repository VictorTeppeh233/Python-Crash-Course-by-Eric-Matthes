#Assignment 4.8
#Cubes: A number raised to the third power is called a cube. 
#For example,the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (thatis, the cube of each integer from 1 through 10)
#Use a for loop to print out the value of each cube.

cube =[]

for num in range(1,11):
    cube.append(num**3)

print(cube)