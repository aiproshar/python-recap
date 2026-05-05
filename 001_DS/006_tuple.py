"""
Tuple: Immutable, ordered iterable. That's all.
       Modifying a tuple creates a new reference.
       Keys takeaway: It's the COMMA that makes a tuple, not parentheses.
"""

# ===========================================================================
# CREATING TUPLES
# ===========================================================================

point = (1, 2)
another_point = 1, 2  # parentheses are optional — comma makes the tuple
single_point = (1,)  # trailing comma needed for single element
empty_tuple = ()

# tuple() accepts any iterable — string, list, range, etc.
name = "Arafat"
name_tuple = tuple(name)
print(name_tuple)  # ('A', 'r', 'a', 'f', 'a', 't')

from_list = tuple([1, 2, 3])
from_range = tuple(range(5))
print(from_list)  # (1, 2, 3)
print(from_range)  # (0, 1, 2, 3, 4)

# ===========================================================================
# IMMUTABILITY — tuples cannot be modified in place
# ===========================================================================

try:
    print(f"Current first item: {name_tuple[0]}")
    name_tuple[0] = 100
except TypeError as e:
    print(f"Failed to modify tuple: {e}")

# "Modifying" a tuple means creating a NEW one
original = (1, 2, 3)
modified = original + (4, 5)  # new tuple, original unchanged
print(original)  # (1, 2, 3)
print(modified)  # (1, 2, 3, 4, 5)
print(original is modified)  # False — different object

# ===========================================================================
# INDEXING & SLICING — same as list
# ===========================================================================

t = (10, 20, 30, 40, 50)
print(t[0])  # 10
print(t[-1])  # 50
print(t[1:3])  # (20, 30)
print(t[::-1])  # (50, 40, 30, 20, 10) — reversed

# ===========================================================================
# TUPLE METHODS — only two, because immutable
# ===========================================================================

t = (1, 2, 3, 2, 2, 4)
print(t.count(2))  # 3 — how many times 2 appears
print(t.index(3))  # 2 — first index of value 3

# ===========================================================================
# PACKING & UNPACKING (behind the scenes)
# ===========================================================================
#
# When Python sees:    x, y, z = y, z, x
#
# Step 1 — PACK the right side into a tuple:
#     temp = (y, z, x)       # evaluates ALL values first
#
# Step 2 — UNPACK that tuple into the left side:
#     x = temp[0]
#     y = temp[1]
#     z = temp[2]
#
# This is why swaps work without a temp variable.

x = 10
y = 11
z = 12
x, y, z = y, z, x
print(x, y, z)  # 11 12 10

# --- Unpacking with * (star) ---
first, *middle, last = (1, 2, 3, 4, 5)
print(first)  # 1
print(middle)  # [2, 3, 4] — star collects into a list
print(last)  # 5


# --- Unpacking in function returns ---
def get_user():
    return "Alice", 30, "NYC"  # returns a tuple


name, age, city = get_user()
print(name, age, city)  # Alice 30 NYC

# --- Ignore values with _ ---
name, _, city = get_user()  # don't care about age
print(name, city)  # Alice NYC

# ===========================================================================
# TUPLE AS DICT KEY — because it's hashable (immutable)
# ===========================================================================

locations = {
    (40.7, -74.0): "New York",
    (51.5, -0.1): "London",
}
print(locations[(40.7, -74.0)])  # New York

# Lists can't be dict keys — they're mutable, so not hashable
# {[1, 2]: "value"}  → TypeError: unhashable type: 'list'

# ===========================================================================
# NAMED TUPLE — tuple with names for readability
# ===========================================================================

from collections import namedtuple

Color = namedtuple("Color", ["r", "g", "b"])
red = Color(255, 0, 0)
print(red.r)  # 255 — access by name
print(red[0])  # 255 — still works by index
print(red)  # Color(r=255, g=0, b=0)

# ===========================================================================
# TUPLE vs LIST — when to use which
# ===========================================================================
#
# Tuple                              List
# --------------------------------   --------------------------------
# Immutable                          Mutable
# Hashable (can be dict key)         NOT hashable
# Slightly faster                    Slightly slower
# Fixed data (coordinates, RGB)      Dynamic data (shopping cart)
# Signals "this won't change"        Signals "this may grow/shrink"
# Returned by many builtins          General purpose workhorse
#   (.items(), enumerate, zip)
