#Modifying Values in a Dictionary
alien = {'x_position': 0, "y_position": "25", 'speed': 'medium'}
print(f'Original position: {alien['x_position']}')

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien['x_position'] = alien['x_position'] + x_increment

print(f'New position: {alien['x_position']}')

alien["speed"] = 'fast'

print(alien)