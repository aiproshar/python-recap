"""
Just generate random stuffs
Super needed, for example every secure connection depends how random you can be
"""

import random
import string

print(random.random())  # returns a random float

# generate a number between 1 and 100
# subsequent run will result in different value unlike C, python seeds using the timestamp when module is imported
print(random.randint(1, 100))

# We want a pin of 4 digits, pin is usually made of numbers
"""
random.choice() -> no K field, k is fixed as 1. returns a single item
random.choices() -> has k field, default 1. K means output char count. returns a list
"""
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=4))

# choices takes any iterable. we can also give it a string
# Lets generate a 8 digit long password with lower alphabets and numbers
print(random.choices("abcdefghijklmonopqrstuvwxyz1234567890", k=8))

# let's generate a real world password generator, with upper lower numeric and special char
char_set = string.ascii_letters + string.digits + string.punctuation
suggested_password = random.choices(char_set, k=12)
# standard way to convert any iterable to string
suggested_password = "".join(suggested_password)
print(f"suggested strong password is: {suggested_password}")

# Random shuffle, change order of items
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(nums)  # in place shuffle, only mutable data structure works
print(nums)
