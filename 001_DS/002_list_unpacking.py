"""
Important concept, this can reduce complexity and beautify code a lot
"""

number = [1, 2, 3]
x, y, z = number
print(f"x is: {x}, y is: {y}, z is: {z}")

# What if we want now only first two items and rest later, or we don't know many of them will be there
many_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
Below is both packing and unpacking, we unpacked on the first and second
And we packed the remaining items in rest
"""
first, second, *other = many_numbers
print(f"first number: {first} second number: {second}, and rest: {other}")

first, *other, last = many_numbers
print(f"first number: {first} last number: {last}, and middle ones: {other}")
