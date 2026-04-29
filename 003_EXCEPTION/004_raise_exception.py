"""
Deliberately raising an exception, obviously based on business logic
We want error to be handled by the caller, so we propagate an exception
Choosing the right type matters and also the exception
"""


def calculate_birth_year(age: int):
    if age < 0:
        # We will raise built-in exception
        # More on 002_exception_types.py
        raise ValueError("Age cannot be negative")
    return 2026 - age


try:
    print(f"Birth year of age 25: {calculate_birth_year(25)}")
    print(f"Birth year of age -1: {calculate_birth_year(-1)}")
except ValueError as e:
    print(f"Exception occurred: {e.__class__.__name__}:{e}")


# More in depth if you want: raising cost is expensive
# The with statement, which is wrapper around context manager protocol __enter__ and __exit__
# Goggle/Claude to more know these in depth
