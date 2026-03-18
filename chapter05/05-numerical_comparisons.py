#Using and to Check Multiple Conditions

#To check whether two conditions are both True simultaneously, 
#use the keyword and to combine the two conditional tests; 
#if each test passes, the overall expression evaluates to True. 
#If either test fails or if both tests fail, the expression evaluates to False.

print("age_0 = 22")
age_0 = 22

print("age_1 = 18")
age_1 = 18

print("checking if both ages are above 20")
print(age_0 >= 20 and age_1 >= 20)

print("checking if both ages are below 25")
print(age_0 <= 25 and age_1 <= 25)


