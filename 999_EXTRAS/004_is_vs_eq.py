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
# UNDER THE HOOD: What == actually does (simplified dispatch)
# ===========================================================================
# When python sees: a == b
# 1. Call type(a).__eq__(a, b)
# 2. If that returns NotImplemented, try type(b).__eq__(b, a)
# 3. If both return NotImplemented, fall back to identity (is)


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
#  ==        | equality       | __eq__ method dispatch | YES        | slower
#
#  Use 'is' for:     None, True, False, sentinel objects
#  Use '==' for:     numbers, strings, lists, dicts, custom objects
#  NEVER rely on:    'is' for integers/strings (interning is implementation detail)
