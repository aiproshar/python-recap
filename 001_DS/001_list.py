"""PROLOGUE

Python data structures: mutable vs immutable

Immutable (int, str, tuple, frozenset):
    Can't be modified in place. Any "change" creates a new object.
    Safe to pass around — no one can alter your original.

Mutable (list, dict, set):
    Modified in place. If you pass a list to a function,
    and it appends to it, your original list changes too.
    Pass a copy if you want to be safe.

Python always passes by object reference — NOT like C++ value vs ref.
The difference is whether the object itself allows mutation,
not how it's passed.

"""

"""
--------------- LIST----------------
An ordered mutable collection of items, that can hold any type
Backed by dynamic array, tail growing on constant time
list[x] read/write -> O(1)
len(x) -> O(1)
list.append() -> O(1) [Amortized, for N appends it will take O(N) time]
list.insert() -> O(n) [Assuming inserting on 0th index everytime)
"""
lst: list[
    int
] = []  # creating list with type hint 'lst = list[int]' is wrong, it's a type alias
lst.append(1)
print(f"List with one item: {lst}")
lst_new = [0] * 5
print(f"[0] * 5 : {lst_new}")

# Let's convert a string to list
name = "Arafat Khan"
name_list = list(name)
print(f'"{name}" in lost rep: {name_list}')

# Accessing list items
letter = ["a", "b", "c", "d", "e"]
print(f"first letter: {letter[0]}")
print(
    f"last letter: {letter[-1]}"
)  # -1 means first last item, -2 means second last item
letter[4] = "E"
print(f"last letter modified: {letter[-1]}")

"""  SLICING

# Slicing [start:stop:step]

if step is negative means we travel reverse, default value is 1
if start and stop is invalid (10:5:1) then return empty list
2:5 means from second index upto 5, not including 5th position

Also slicing is forgiving, it doesn't return an error. Returns empty slice
[ default->0: default->len(list)], that's why we go upto 
"""


print(letter[2:200])  # No error although it has only 0-4 index, returns valid array
print(letter[-100:100:-32])  # Totally nonsense but no error

list_nums = list(
    range(1, 101)
)  # list takes any iterable and iterates and constructs the list
print(list_nums[1::2])  # 2 -> 100 all even numbers, we started from 0, 2 as step
