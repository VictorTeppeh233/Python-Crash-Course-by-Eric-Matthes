# assignment 9.11

"""
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, 
and call show_privileges() to show that everything is working correctly.
"""

from admin import User, Privileges , Admin

my_admin = Admin('albert', 'einstein', 'aeinstein@gmail.com', 'aeinstein', 3 )

my_admin.privileges.show_privileges()