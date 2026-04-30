"""
Static method: a method that lives in the class namespace but doesn't take self or cls
It's just a regular function, the class is only acting as a container/grouping

Quick comparison:
- instance method: first param is `self`     -> needs an instance, can read/write instance state
- @classmethod:    first param is `cls`      -> no instance needed, can read/write class state (factories)
- @staticmethod:   no special first param    -> no instance, no class. Pure function bolted onto the class

When to use it:
- The function is logically related to the class but doesn't depend on instance OR class state
- A helper/utility that you want grouped with the class for discoverability
- Could be a module-level function, but namespacing it on the class makes the relationship obvious

If you find yourself never touching self/cls inside a method, that's the signal — make it static
"""

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[X:{self.x}] [Y:{self.y}]"

    # Classmethod: factory, uses cls so subclasses get the right type back
    @classmethod
    def default(cls):
        return cls(0, 0)

    # Staticmethod: no self, no cls. Just a helper that conceptually belongs to Point2D
    # Distance is a property OF points, but computing it doesn't need any one point's state
    @staticmethod
    def distance(p1, p2) -> float:
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


# Static methods can be called from the class OR from an instance — both work
# Calling from the class is preferred, makes intent clearer

a = Point2D(0, 0)
b = Point2D(3, 4)

# Class-level call (preferred)
print(f"Distance: {Point2D.distance(a, b)}")

# Instance-level call also works, but reads weirdly — `a` is not used inside distance()
print(f"Distance: {a.distance(a, b)}")


"""
We mostly use static method as helper function, which does not affect any state
It's a pure function — same input always gives same output, no side effects
Class method can behave similar to static method if it doesn't read or modify class attributes
You might wonder how just *reading* breaks purity. Imagine the class keeps a count of
active instances. A `current_instance_count` classmethod doesn't modify any state, but
its result changes over time as instances are created/destroyed — so it's not pure.
"""
