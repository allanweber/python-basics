square = [x * x for x in range(10)]
print(square)

square2 = []
for x in range(10):
    square2.append(x * x)
print(square2)

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)