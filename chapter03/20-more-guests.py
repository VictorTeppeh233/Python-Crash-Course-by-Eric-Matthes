#Assignment 3.6
#Start with your program from Exercise 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

dinner_list = ["Sena", "Felicity", "Karen", "Naomi", "Vanessa"]
print(dinner_list)


dinner_list.insert(0, "Salma")

dinner_list.insert(3, "Joshua")

dinner_list.append("Sylvia")

print(f"Dear {dinner_list[0].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[1].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[2].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[3].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[4].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[5].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[6].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[7].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"I have found a bigger table we could use for our dinner")