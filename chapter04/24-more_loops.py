#Assignment 4.12

# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

#adding different foods to each list
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My foods")
for food in my_foods:
    print(food.title())

print("Friend's food")
for food in friend_foods:
    print(food.title())