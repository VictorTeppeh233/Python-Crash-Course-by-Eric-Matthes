#Using get() to Access Values

alien = {'color': 'green', 'speed': 'slow'}

point_value = alien.get('points', "No point value assigned.")
print(point_value)