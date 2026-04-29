import math


class Point2D:  # Defining A class blueprint, naming convention: MyPoint (no underscore, first latter upper case)
    # Self is always the very first param in every method

    def print(self):
        print(f"co-ordinates: {self.x}, {self.y}")

    # Return type hint (static/structural — opposite of duck typing)
    def radius(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __init__(self, x, y):  # Magic Method constructor
        self.x = x
        self.y = y

    """
	Python does not support method overloading, so there cannot be another
	__init__(self): with no zero params (or one because self is always there)
	The recommended way is to use @classmethod. More on next file
	"""

    # More on this on 003, this is magic method
    def __str__(self):  # important, this is called by the print method
        return f"[X:{self.x}] [Y:{self.y}]"

    def future(self):
        pass  # by pass, we are escaping error, but must be implemented in the future


def main():

    example_point = Point2D(100, 100)
    example_point.print()
    print(f"Value of example point: {example_point}")
    print(f"Radius of example point: {example_point.radius()}")

    # Some helper function

    print(type(example_point))  # <class '__main__.Point2D'> -> main is our module name
    print(type(Point2D))  # <class 'type'>
    print(isinstance(example_point, Point2D))  # true

    # Let's create another point object
    another_point = Point2D(2, 2)
    example_point.print()
    print(f"Value of example point: {example_point}")
    print(f"Radius of example point: {example_point.radius()}")


if __name__ == "__main__":
    main()
