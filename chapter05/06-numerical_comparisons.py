#Using or to Check Multiple Conditions

'''
The keyword or allows you to check multiple conditions as well, but it passes
when either or both of the individual tests pass. An or expression fails only
when both individual tests fail.
'''

print("age_0 = 22")
age_0 = 22

print("age_1 = 18")
age_1 = 18

print("checking if either ages are above 20")
print(age_0 >= 20 or age_1 >= 20)

print("checking if both ages are below 15")
print(age_0 <= 15 or age_1 <= 15)