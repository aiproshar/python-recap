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


# Looping over list, just items
for item in many_numbers:
    print(f"{item}")
"""
for item in enumerate(many_numbers): -> in each iteration they will return a tuple, we unpack this
    print(f"index: {item[0} item: {item[1]}")

Better example below
"""
for idx, item in enumerate(many_numbers):
    print(f"index: {idx} item: {item}")

# Adding and removing items
# End of the list -> super easy, constant time operation
lst = [1, 2, 3, 4]
lst.pop()  # removes ith item, default -1, means last item
lst.append(5)
print(lst)
lst.pop(0)  # O(n) very inefficient
print(lst)

"""
Searching for item, does 'a' exist ? where ?
Be careful, python returns value error when item is not present
"""

lst = [1, 2, 3, 4, 5]
print(
    lst.index(3)
)  # Prints the first occurrence, [1,2,3,4,3,3,3,3] will also return same

try:
    print(lst.index(100))
except ValueError as e:
    print(f"Got value error because item does not exists: {e}")
# The pythonic way to find index

query = 3
if 3 in lst:
    print(f"3 is present, position: {lst.index(3)}")
else:
    print("3 is not present")


"""
sorting a list
"""
nums = [1, 7, 5, 9, 3, 4, 2]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
