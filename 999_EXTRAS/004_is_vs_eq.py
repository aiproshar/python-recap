"""
is vs == : Identity vs Equality

is  → compares memory address (pointer comparison in CPython)
==  → calls __eq__ dunder method, can be overridden

Rule: use 'is' for None, True, False (singletons)
      use '==' for everything else (value comparison)
"""

# ===========================================================================
# BASIC DIFFERENCE
# ===========================================================================

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b : {a == b}")  # True  — same contents
print(f"a is b : {a is b}")  # False — different objects in memory
print(f"a is c : {a is c}")  # True  — c points to the same object as a
print(f"id(a): {id(a)}  id(b): {id(b)}  id(c): {id(c)}")


# ===========================================================================
# WHY IT MATTERS FOR None
# ===========================================================================
# None is a singleton — exactly one NoneType object exists in the interpreter
# 'is None' does a fast pointer check, no method dispatch
# '== None' calls __eq__, which can be hijacked


class Sneaky:
    def __eq__(self, other):
        return True  # claims to equal everything


s = Sneaky()
print(f"\ns == None : {s == None}")  # True  — __eq__ lied
print(f"s is None : {s is None}")  # False — pointer check, can't be fooled


# ===========================================================================
# REAL WORLD: SQLAlchemy-style __eq__ OVERRIDE
# ===========================================================================
# Libraries override __eq__ to build expressions, not return booleans


class Column:
    """Mimics how ORMs override == to produce SQL clauses"""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        # Returns a string expression instead of True/False
        return f"{self.name} IS NULL" if other is None else f"{self.name} = '{other}'"


username = Column("users.name")
result = username == None
print(f"\nColumn == None returned: {result}")  # "users.name IS NULL" — not a bool!
print(f"type: {type(result)}")  # <class 'str'>

result2 = username == "alice"
print(f"Column == 'alice' returned: {result2}")  # "users.name = 'alice'"


# ===========================================================================
# INTERNING GOTCHA: SMALL INTEGERS AND SHORT STRINGS
# ===========================================================================
# CPython caches (interns) small integers [-5, 256] and some short strings
# so 'is' may accidentally return True for equal values
# This is an implementation detail, NEVER rely on it

x = 256
y = 256
print(f"\n256 is 256 : {x is y}")  # True  — cached, same object

x = 257
y = 257
print(f"257 is 257 : {x is y}")  # False — outside cache range, different objects
# Both have value 257, but they are different objects in memory
print(f"257 == 257 : {x == y}")  # True  — value comparison works correctly

# Same gotcha with strings
a = "hello"
b = "hello"
print(f"\n'hello' is 'hello' : {a is b}")  # True — interned (short, identifier-like)

a = "hello world!"
b = "hello world!"
print(
    f"'hello world!' is 'hello world!' : {a is b}"
)  # False — not interned (has space and !)
print(f"'hello world!' == 'hello world!' : {a == b}")  # True  — value check works


# ===========================================================================
# SINGLETONS IN PYTHON
# ===========================================================================
# Python guarantees exactly ONE instance of these objects:
#   - None   (NoneType)
#   - True   (bool)
#   - False  (bool)
#
# Since there's only one of each, 'is' is the correct check:
#   x is None       ✅
#   x is True       ✅  (though 'if x:' is usually preferred)
#   x == None       ❌  (can be hijacked by __eq__)
#
# SENTINEL PATTERN — create your own singleton for "missing value":

_MISSING = object()  # unique object, will never compare equal to anything else


def get(key, default=_MISSING):
    """Distinguish 'no default given' from 'default is None'."""
    data = {"a": 1, "b": None}
    if key in data:
        return data[key]
    if default is _MISSING:  # 'is' check, just like None
        raise KeyError(key)
    return default


print(f"\nget('b')       : {get('b')}")  # None — key exists, value is None
print(f"get('z', 42)   : {get('z', 42)}")  # 42   — key missing, default used
try:
    get("z")  # no default → raises KeyError
except KeyError:
    print("get('z')       : KeyError raised")  # key missing, no default


# ===========================================================================
# HASHING: __hash__ AND __eq__ AS A PAIR
# ===========================================================================
# Sets and dicts use a two-step lookup:
#   Step 1: __hash__() → picks which BUCKET to look in        (O(1))
#   Step 2: __eq__()   → checks items IN that bucket for match (O(1) usually)
#
# Think of it like an apartment building:
#   __hash__ → which floor to go to
#   __eq__   → which door on that floor
#
# THE CONTRACT (must ALWAYS hold):
#   if a == b, then hash(a) == hash(b)
#
# The reverse is NOT required — different objects CAN share a hash (collision).
# But if equal objects had different hashes, they'd land in different buckets
# and the set would silently fail to find them.

# --- Default behavior for custom classes (inherited from object) ---
# __hash__  → based on id() (memory address)
# __eq__    → based on 'is' (identity)
# Result: each instance is unique in a set, even with same .val


class Node:
    def __init__(self, val):
        self.val = val


a = Node(5)
b = Node(5)

print(f"\nhash(a) == hash(b) : {hash(a) == hash(b)}")  # False — different objects
print(f"a == b             : {a == b}")  # False — identity check
print(f"a in {{a, b}}        : {a in {a, b}}")  # True  — same object found

# This is exactly why storing Node objects in a set works for cycle detection:
#   seen = set()
#   seen.add(current)       # hash(current) → bucket based on id
#   if current in seen:     # finds EXACT same node, not just same value

# --- What happens when you override __eq__ without __hash__? ---


class BadNode:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return isinstance(other, BadNode) and self.val == other.val

    # forgot __hash__!


# Python makes this UNHASHABLE to prevent silent bugs:
try:
    s = {BadNode(1)}  # TypeError!
except TypeError as e:
    print(f"\nBadNode in set: {e}")

# --- Correct override: define BOTH ---


class GoodNode:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return isinstance(other, GoodNode) and self.val == other.val

    def __hash__(self):
        return hash(self.val)  # consistent: equal objects → same hash


x = GoodNode(5)
y = GoodNode(5)
print(f"\nGoodNode: x == y       : {x == y}")  # True  — value match
print(f"GoodNode: hash(x)==hash(y): {hash(x) == hash(y)}")  # True  — contract holds
print(f"GoodNode: x in {{y}}     : {x in {y}}")  # True  — found via value


# ===========================================================================
# THE 'in' OPERATOR — DIFFERENT BEHAVIOR PER CONTAINER
# ===========================================================================
# 'in' is NOT one operation — it depends on what you're searching:
#
# CONTAINER   | MECHANISM                    | COMPLEXITY
# ------------|------------------------------|----------
# list/tuple  | walks each item, calls ==    | O(n)
# set/dict    | hash → bucket, then ==       | O(1) avg
# string      | substring search             | O(n)
#
# This is WHY you use a set (not a list) for visited-node tracking:

import time

big_list = list(range(100_000))
big_set = set(range(100_000))

target = 99_999  # worst case for list

start = time.perf_counter()
_ = target in big_list
list_time = time.perf_counter() - start

start = time.perf_counter()
_ = target in big_set
set_time = time.perf_counter() - start

print(f"\n99999 in list : {list_time * 1000:.4f} ms")  # slow — scans all items
print(f"99999 in set  : {set_time * 1000:.4f} ms")  # fast — hash lookup

# String 'in' is completely different — substring search:
print(f"\n'he' in 'hello' : {'he' in 'hello'}")  # True — substring
print(f"'xyz' in 'hello' : {'xyz' in 'hello'}")  # False


# ===========================================================================
# UNDER THE HOOD: What == actually does (simplified dispatch)
# ===========================================================================
# When python sees: a == b
# 1. Call type(a).__eq__(a, b)
# 2. If that returns NotImplemented, try type(b).__eq__(b, a)
# 3. If both return NotImplemented, fall back to identity (is)
#
# NOTE: NotImplemented (a singleton value) is NOT the same as
#       NotImplementedError (an exception). Common interview gotcha.


class Left:
    def __eq__(self, other):
        print("  Left.__eq__ called")
        return NotImplemented  # "I don't know how to compare with this"


class Right:
    def __eq__(self, other):
        print("  Right.__eq__ called")
        return True


print("\nDispatch order demo:")
result = Left() == Right()
# Left.__eq__ called first, returns NotImplemented
# Python then tries Right.__eq__, which returns True
print(f"Result: {result}")


# ===========================================================================
# NONE CHECK: ALWAYS USE 'is'
# ===========================================================================


def fetch_user(user_id):
    """Returns None if user not found"""
    if user_id == 0:
        return None
    return {"id": user_id, "name": "Arafat"}


user = fetch_user(0)

# ✅ Correct — fast, safe, can't be overridden
if user is None:
    print("\nUser not found (is None)")

# ❌ Wrong — works here but breaks if user's type overrides __eq__
if user == None:
    print("User not found (== None)")

# Same applies to 'is not None'
user = fetch_user(1)
if user is not None:
    print(f"Found user: {user['name']}")


# ===========================================================================
# QUICK REFERENCE
# ===========================================================================
#
#  Operator  | Checks         | Mechanism              | Override?  | Speed
#  ----------|----------------|------------------------|------------|-------
#  is        | identity       | pointer comparison     | NO         | fastest
#  ==        | equality       | __eq__ method dispatch  | YES        | slower
#  hash()    | bucket index   | __hash__ method         | YES        | fast
#  in (list) | membership     | linear scan + __eq__    | via __eq__ | O(n)
#  in (set)  | membership     | __hash__ + __eq__       | via both   | O(1)
#  in (str)  | substring      | search algorithm        | NO         | O(n)
#
#  Use 'is' for:     None, True, False, sentinel objects
#  Use '==' for:     numbers, strings, lists, dicts, custom objects
#  NEVER rely on:    'is' for integers/strings (interning is implementation detail)
#
#  HASHING CONTRACT:
#    if a == b → hash(a) MUST == hash(b)       (required)
#    hash(a) == hash(b) → a MAY != b           (collisions are allowed)
#    override __eq__ → MUST also override __hash__ (or object becomes unhashable)
