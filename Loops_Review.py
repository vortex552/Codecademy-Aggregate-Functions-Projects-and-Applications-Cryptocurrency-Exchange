single_digits = range(0, 10)
squares = []
cubes = [digit**3 for digit in single_digits]
for digit in single_digits:
  squares.append(digit**2)
print(squares)
print(cubes)
