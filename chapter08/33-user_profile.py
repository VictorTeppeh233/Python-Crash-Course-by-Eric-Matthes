# assignment 8.13

"""
Start with a copy of user_profile.py. 
Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you.
"""

#creating the function
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_proifle = build_profile('victor', 'teppeh',
                             location='accra',
                             field='ai',
                             hobby='chess')
print(user_proifle)