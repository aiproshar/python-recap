"""
One of the most important things, we must know all string operations
You will mess up interview if you forget a small library function
Review before each interview


---------------- STRING ----------------
Immutable sequence of character, constant time random element access
Every state change in a string generates a new string
"""

from os import supports_effective_ids

s = "arafat khan"
print(f'string: "{s}" Len: {len(s)} id: {id(s)}')  #
# Lets capitailize This

try:
    s[0] = "A"
except TypeError as e:
    print("unable to capitalize first letter: ", e)

## OOps, i told you string is immutable, but how we do this ?
# Convert to mutable list, edit and create again
s_list = list(s)  # list takes any iterable, string is iterable YaY
s_list[0] = "A"
s_new = "".join(s_list)
print(f'new string: "{s_new}" Len: {len(s_new)} id: {id(s_new)}')  #

# We can also do slicing here
s_another = "A" + s[1:0]
print(f'another string: "{s_another}" Len: {len(s_another)} id: {id(s_another)}')  #

print(
    f"first 5 word: {s_another[:5]}"
)  # 0 upto 5, means 0,1,2,3,4 s[0:len(s)] == s[::] is default
print(
    f"Invalid Slice s[1000:2000] and no error: {s[1000:2000]}"
)  # slice is forgiving everywhere
s = "1234567"
for char in s:  # niteration
    print(char)
print("\n")
for char in s[::-1]:  # pythonic reverse iteration
    print(char)
# Replace middle item, make 5 -> X
s_mod = s[:4] + "x" + s[5:]  # End index always upto
print(f"1234567 -> 5 is replaced by x: {s_mod}")

first = "Arafat"
last = "Khan"
name = first + " " + last  # extreamly expensive, builds over each time
print(f"concat name: {name}")

"""
Building strings with += in a loop is O(n²). Every += creates a new string,
copies everything over. For N characters that's N + (N-1) + (N-2)... = O(n²)

Do all your operation on a list, use deque so you can push pop both end and also change inplace constant time
convert the list to string in very end, if you afraid of lists immutability, use list.copy() when passing to another function
"""

# Do O(n²)
result = ""
for ch in "abcdef":
    result += ch  # new string every iteration

# Avoid O(n)
parts = []
for ch in "abcdef":
    parts.append(ch)
result = "".join(parts)

"""
------------- ORD and CHAR---------------
ord(char) → integer (Unicode code point)
chr(int)  → character
ASCII you need to memorize:
    'a' = 97,  'z' = 122
    'A' = 65,  'Z' = 90
    '0' = 48,  '9' = 57
"""

# Get position of letter in alphabet (0-indexed). This comes up ALL the time.
char = "f"
pos = ord(char) - ord("a")  # 5
print(f"'{char}' is at position {pos}")

# int to char
print(f"char for 97 is: {chr(97)}")

# Manual char range check
c = "G"
is_upper = ord("A") <= ord(c) <= ord("Z")
is_lower = ord("a") <= ord(c) <= ord("z")
is_digit = ord("0") <= ord(c) <= ord("9")
print(f"'{c}' upper:{is_upper} lower:{is_lower} digit:{is_digit}")

"""
------------ CASE OPERATIONS
"""
s = "hello Workd 88Nn ##ad 12nd 12VV"
s_lower = s.lower()  # all lower
s_upper = s.upper()  # All upper
s_title = (
    s.title()
)  # First alphabet of each word, ignores non alphabets #s"12aa".title() -> #12Aa
print(s)
print(s_lower)
print(s_upper)
print(s_title)


"""
search (reverse index): give me index of this item (if exists)
index -> dangerous, raises valueError exception
find -> safer function, returns -1 if not found, but can have silent bugs. because in slice -1 means last item. If you slicing based on find, be careful
"""
s = "12345"
print(s[3])
print(s[-1])  # last item, -2: second last item

# out of bounds throws index error
try:
    print(s[1000])
except IndexError as e:
    print(f"Error accessing: {e}")

text = "hi apple banana mango all are my fav fruits, 1 apple a day"
# Search for item, starts scanning from left and returns first
print(f"looking for apple index: {text.find('apple')}")
print(f"looking for watermelon index: {text.find('watermelon')}")
try:
    print(f"looking for watermelon index: {text.index('watermelon')}")
except ValueError as e:
    print(f"Exception occurred in text.index(), {e}")

# what if we want to search from right side to left (reverse traverse) to find index
# We can use rfind
text = "hi apple banana mango all are my fav fruits, 1 apple a day"
print(f"looking for apple index from the last: {text.rfind('apple')}")

# Count: non-overlapping occurrences
# aaaa.count(aa) -> 2, not 3
# We can also use start, end like slice (but in place)

text = "hi apple banana mango all are my fav fruits, 1 apple a day"
print(f'looking for number of occurrences of "apple": {text.count("apple")}')

"""
There is also an in operator, just like set/key/list, it also works on string
in operator O(1) if has __contains__ method, otherwise iterate to find it
"""
if "apple" in text:  # O(n) but fast
    print(f"We are sure apple is in text, freq: {text.count('apple')}")

"""
Character type check
"""
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # letters or digits
print(f"'abc'.isalpha():    {'abc'.isalpha()}")  # letters only
print(f"'123'.isdigit():    {'123'.isdigit()}")  # digits only
print(f"'   '.isspace():    {'   '.isspace()}")  # whitespace only

""" 
----------------------------- STRIP----------------------------

strip -> strip both ends. Default is whitespace
lstrip, rstrip -> strips from sides only
all strip takes a charset as optional argument, will strip those from end(s)
"""
bad_text = "   This is a text with spaces both end   "
print(f'strip both ends: "{bad_text.strip()}"')
print(f'strip left end: "{bad_text.lstrip()}"')
print(f'strip right end: "{bad_text.rstrip()}"')
print("\n\n")
noisy_text = " ###..real #. text..  .# #"
print(f'strip noise from both ends: "{noisy_text.strip(" #.")}"')
print(f'strip noise from left end: "{noisy_text.lstrip(" #.")}"')
print(f'strip noise from right end: "{noisy_text.rstrip(" #.")}"')


"""
------------------------------SPLIT-----------------------------------

str.split() -> splits based on empty space, also removes any whitespace
str.split(',') -> split based on comma, can have empty string
"""
csv = "a,b,c,d,e"
csv_corrupt = "a,b,c,,d,   e"
print(f"clean split: {csv.split(',')}")
print(f"corrupt has empty and spaces: {csv_corrupt.split(',')}")

# second parameter: how many times we want to split. default -1, means unlimited
print(f"split max 2 from left:  {csv.split(',', 2)}")

# rsplit -> splits from right to left. If no maxsplit is given, it is exactly same as split
print(f"split max 2 from right: {csv.rsplit(',', 2)}")

# splitlines -> splits based on  \n \r\n \e
multiline_text = """
hi i am arafat \n new line
this is new line in formatting
its okay \r\n now that


its okay \r\r\r nnn
"""
print(multiline_text.splitlines())  # also prints empty string
