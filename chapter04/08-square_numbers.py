#creating the first 10 square numbers into a list:

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)