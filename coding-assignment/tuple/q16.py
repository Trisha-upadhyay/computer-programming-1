nested = ((1, 2), (3, 4), (5, 6))
flattened = tuple(num for group in nested for num in group)
print(flattened)  # Output: (1, 2, 3, 4, 5, 6)
