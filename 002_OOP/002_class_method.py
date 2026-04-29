import math


class Point2D:  # Defining A class blueprint, naming convention: MyPoint (no underscore, first latter upper case)
    # Self is always the very first param in every method

    # Shared among all the instance
    default_color = "RED"  # This is a class attribute

    def print(self):
        print(f"co-ordinates: {self.x}, {self.y}")

    def radius(self) -> float:  # type-hinted return
        return math.sqrt(self.x**2 + self.y**2)

    # Magic Method constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # A class attribute, you can call it from class ref
    # Instead of method overloading for many constructors, this is pythonic way
    # Default factory method
    # For each cls method, the first param is cls object.
    @classmethod
    def default(cls):
        return cls(0, 0)


example_point = Point2D(1, 2)

# First search in the instance attribute then class attribute
print(example_point.default_color)
# Now lets change the class attribute
Point2D.default_color = "New Red"

# Printing updated class attribute
print(example_point.default_color)


# But if you edit class attribute from an instance, it will create a new instance attribute
example_point.default_color = "instanceColor"

latest_point = Point2D.default()

print(example_point.default_color)
print(latest_point.default_color)
