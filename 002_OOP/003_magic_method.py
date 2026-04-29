"""
MAGIC METHOD

__method_name__ , starts and ends with __
inherited from object, every class inherits object
'class Circle' is actually 'class Circle(object)'
These are implemented, rest are not. That's why you will get an error if you try to compare custom class


__init__      # does nothing, just returns None
__new__       # creates the instance in memory
__eq__        # compares by memory address (is)
__ne__        # opposite of __eq__
__hash__      # returns unique hash based on id
__str__       # returns "<ClassName object at 0x...>"
__repr__      # same as __str__ by default
__bool__      # always returns True
__getattribute__  # handles attribute access
__setattr__   # handles setting attributes
__delattr__   # handles deleting attributes
__dir__       # lists available attributes/methods
__class__     # returns the class
__sizeof__    # returns memory size
__format__    # handles format() calls
__reduce__    # for pickling/serialization
__reduce_ex__ # for pickling/serialization

Important ones that are not implemented, will raise TypeError
__add__, __sub__, __mul__, __lt__, __gt__, __len__ and similar


Summary
# 1. Implemented with default behavior (on object) and can cause bugs, be careful
__eq__       # works, compares by memory address
__str__      # works, prints memory location

# 2. Not implemented, but NOT enforced (not on object)
__add__      # just doesn't exist, errors only if you try to use +
__len__      # just doesn't exist, errors only if you call len()

"""


class Circle:
    # Constructor magic method
    def __init__(self, x: float, y: float, radius: float):
        self.radius = radius
        self.x = x
        self.y = y

    # __srt__ is called in print, default prints memory location
    def __str__(self):
        return f"[{self.x}:{self.y}]-> {self.radius}"

    # default __eq__ only compares memory location, different object return false
    def __eq__(self, other) -> bool:
        # Important AF, Different class object with similar attribute can return true
        # Make sure they are from same class first
        if not isinstance(
            other, type(self)
        ):  # isinstance(other, Circle) -> Static definition
            return False
        # Standard pythonic way to compare multiple attribute
        return (self.x, self.y, self.radius) == (other.x, other.y, other.radius)

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return Circle(self.x + other.x, self.y + other.y, self.radius + other.radius)


c1 = Circle(2, 2, 4)

# prints __str__ output
print(c1)

c2 = Circle(7, 4, 2)

print(c1 == c2)

new = c2 + c1
print(new)


"""
There is also some stuff name magic attribute, same idea. Its part of the base object class
Magic attributes can be for class, object, function. Also on modules (we will learn them later)
On objects and classes:

__dict__ — a dictionary of the object's (or class's) writable attributes
__class__ — reference to the object's class
__slots__ — when defined, restricts which attributes an instance can have (and skips __dict__)

On classes specifically:

__bases__ — tuple of direct parent classes
__mro__ — method resolution order (the full inheritance chain)
__name__ — the class name as a string
__subclasses__() — this one's actually a method, but worth noting

On functions:

__name__ — the function's name
__defaults__ — tuple of default argument values
__code__ — the compiled bytecode object
__closure__ — the enclosed variables (for closures)
__annotations__ — type hints dictionary
"""

# Additional important magic methods force context management and cleanup
"""
class Resource:
    def __enter__(self):
        print("Setting up")
        return self  # value bound to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Tearing down")
        return False  # don't suppress exceptions, it will run guaranteed

with Resource() as r:
    print("Using resource")
"""
