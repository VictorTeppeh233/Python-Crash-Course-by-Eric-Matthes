#Assignment 3.5
#Start with your program from Exercise 3.4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

dinner_list = ["Sena", "Samuel", "Felicity", "Karen", "Naomi"]

unavailable = dinner_list.pop(1)

print(f"Unfortunately, {unavailable} would not be able to make it.\n")

dinner_list.append("Vanessa")

print(f"Dear {dinner_list[0].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[1].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[2].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[3].title()}, you are warmly invited to the end of year dinner hosted by Victor.")

print(f"Dear {dinner_list[4].title()}, you are warmly invited to the end of year dinner hosted by Victor.")


