"""
Dictionary: maps keys to values. Keys must be hashable (and in practice,
            immutable). Dict itself is mutable.
            Internally a Hash Table → O(1) average lookup.
            Ordered by insertion since Python 3.7.

Set: Like a dict with only keys, no values. A collection of unique items.
     Items must be hashable (in practice, immutable). Set itself is mutable.
     Immutable version: frozenset.
"""

# ===========================================================================
# DICT
# ===========================================================================

# --- Creating ---
x = dict()
another_x = {}
x_with_items = {"arafat": 29, "irfan": 17}
print(x_with_items["arafat"])  # 29

# --- KeyError on missing key ---
try:
    print(x["arafat"])
except KeyError as e:
    print(f"Got KeyError: {e}")

# --- Safe access patterns ---
# 1. Check first
if "arafat" in x_with_items:
    print(f"Key present, value: {x_with_items['arafat']}")

# 2. Use .get() — returns None by default, or your custom fallback
val = x_with_items.get("not_present", -1)
print(val)  # -1

# NOTE: .get() is a pure read — it NEVER inserts a key.
#       Same behavior in both dict and defaultdict.

# --- Iterating ---
fruit_stock = {"apple": 10, "orange": 23, "melon": 70, "mango": 22, "coconut": 10}

# Default iteration gives keys only
for fruit in fruit_stock:
    print(fruit)

# .items() returns (key, value) tuples, we unpack them
for key, val in fruit_stock.items():
    print(f"Key: {key} Value: {val}")

# enumerate wraps any iterable, returns (index, item) tuple
# item here is itself a (key, val) tuple from .items()
for idx, (key, val) in enumerate(fruit_stock.items()):
    print(idx, key, val)

# sorting items in a dict, required for example top K feq element
fruits_count = {"apple": 10, "banana": 20, "orange": 27, "mango": 25, "guava": 20}
sorted_fruit = sorted(fruits_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_fruit)  # prints a list of tuples
# top K frequent elements needs this
# We want to sort using values, not keys. That's why we must iterate over items


# ===========================================================================
# DEFAULT DICT — returns default value instead of KeyError
# ===========================================================================
#
# The factory is any callable with no arguments:
#   defaultdict(int)          → 0       (because int() == 0)
#   defaultdict(list)         → []      (because list() == [])
#   defaultdict(set)          → set()   (because set() == set())
#   defaultdict(str)          → ""      (because str() == "")
#   defaultdict(float)        → 0.0     (because float() == 0.0)
#
# --- Lambda for custom defaults ---
#   defaultdict(lambda: 1)          → 1
#   defaultdict(lambda: 100)        → 100
#   defaultdict(lambda: "N/A")      → "N/A"
#   defaultdict(lambda: [1, 2, 3])  → [1, 2, 3]
#
# Why lambda? Because int/list/str are just shortcuts for lambda: 0, lambda: [], etc.
# Lambda lets you pick ANY default value you want.

from collections import defaultdict

# --- Basic usage with int ---
counter = defaultdict(int)

# Direct access d[key] → inserts key with default if missing
print(f"Integer default dict value: {counter['no_exist']}")  # 0, key now exists

# Classic use case — counting
fruit_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for fruit in fruit_list:
    counter[fruit] += 1
print(dict(counter))
# {'no_exist': 0, 'apple': 3, 'banana': 2, 'cherry': 1}

# --- Lambda: custom default value ---

# Start counting from 1 instead of 0
counter_from_one = defaultdict(lambda: 1)
counter_from_one["a"] += 1
counter_from_one["b"] += 1
counter_from_one["c"]  # never incremented, stays at default
print(dict(counter_from_one))  # {'a': 2, 'b': 2, 'c': 1}

# Default to a string
status = defaultdict(lambda: "unknown")
status["alice"] = "active"
print(status["alice"])  # "active"
print(status["bob"])  # "unknown" — missing key, lambda kicks in

# --- Lambda: nested defaultdict ---
# Useful for 2D counters like scores[person][subject] = marks
scores = defaultdict(lambda: defaultdict(int))
scores["alice"]["math"] += 90
scores["alice"]["science"] += 85
scores["bob"]["math"] += 70
print(scores["bob"]["science"])  # 0 — both levels auto-create
print(dict(scores["alice"]))  # {'math': 90, 'science': 85}

# IMPORTANT: .get() vs d[key] in defaultdict
# d[key]        → uses factory default (int/lambda/etc), INSERTS the key
# d.get(key)    → returns None, NEVER inserts (pure read, no state change)
# d.get(key, v) → returns v, NEVER inserts (pure read, no state change)

# ===========================================================================
# DICTIONARY COMPREHENSION
# ===========================================================================

values = [x**2 for x in range(1, 11)]  # list comprehension
values_dict = {x: x**2 for x in range(1, 11)}  # same idea, key:value pair
print(values_dict)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# ===========================================================================
# SET — like a dict but only keys, no values
# ===========================================================================

# --- Creating ---
colors = {"red", "green", "blue"}
from_list = set([1, 2, 2, 3])  # {1, 2, 3} — duplicates removed
empty_set = set()  # NOT {} — that creates an empty dict!

# --- Adding & Removing ---
colors.add("yellow")
colors.discard("red")  # safe — no error if missing
colors.remove("green")  # raises KeyError if missing

# --- discard vs remove: both return None, NOT True/False ---
# If you need to know whether something was actually removed:
s = {1, 2, 3}

# Pythonic: check membership first, then discard
if 2 in s:
    s.discard(2)
    print("removed 2")

# Or: use remove() and catch the error
try:
    s.remove(99)
except KeyError:
    print("99 wasn't in the set")

# Summary:
# discard(x)  → missing item silently ignored, returns None
# remove(x)   → missing item raises KeyError,  returns None
# pop()       → removes arbitrary item,        returns the removed item

# --- Set Operations (the real power) ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # union:          {1, 2, 3, 4, 5, 6}
print(a & b)  # intersection:   {3, 4}
print(a - b)  # difference:     {1, 2}
print(a ^ b)  # symmetric diff: {1, 2, 5, 6}

# --- Membership test is O(1) — very fast ---
print("blue" in colors)  # True

# --- Set Comprehension ---
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# --- frozenset — immutable set, can be used as dict key ---
fs = frozenset([1, 2, 3])

# ===========================================================================
# QUICK REFERENCE
# ===========================================================================
#
#  Structure  | Ordered | Mutable | Duplicates | Lookup  | Underlying DS
#  -----------|---------|---------|------------|---------|---------------
#  dict       | yes*    | yes     | keys: NO   | O(1)   | Hash Table
#  defaultdict| yes*    | yes     | keys: NO   | O(1)   | Hash Table
#  set        | NO      | yes     | NO         | O(1)   | Hash Table
#  frozenset  | NO      | NO      | NO         | O(1)   | Hash Table
#
#  * insertion order preserved since Python 3.7
