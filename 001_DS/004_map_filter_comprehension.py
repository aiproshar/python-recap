"""
Map, filter -> transform and accept/reject criteria on each list item
Can work on any iterables
comprehension -> combination of both, most beloved python feature
"""

"""
MAP
"""
people = [
    ["Alice", 29, "Software Engineer", 125000],
    ["Bob", 54, "High School Teacher", 58000],
    ["Charlie", 37, "Registered Nurse", 72000],
    ["Diana", 61, "Postal Worker", 47000],
    ["Ivy", 41, "Pharmacist", 128000],
    ["Jake", 31, "Pilot", 140000],
    ["Karen", 44, "Police Officer", 68000],
    ["Leo", 44, "Plumber", 74000],
    ["Maria", 31, "Physical Therapist", 80000],
    ["Nick", 63, "Janitor", 32000],
    ["Olivia", 23, "UX Designer", 92000],
]
# let's create a list of people with only names and salary
compact_people = []
for name, age, profession, salary in people:
    if salary > 80000:
        name = name.upper()
        compact_people.append((name, salary))
print(f"list of  people who with names and salary: {compact_people}")

"""
We can do this easily in map
syntax: map(function, iterable)
function -> takes an item, returns modified item
lambda is the backbone here. in that case: map(lambda: item: lambda_expression, iterable)
"""

compact_people = map(lambda item: (item[0], item[3]), people)
print(
    f"Trying to print people after map\n {compact_people}"
)  # It returns a lazy iterator map object, so we need to iterate it to see all items
# We need to construct this
compact_people = list(compact_people)
print(f"Again trying to print people after map with list convert\n {compact_people}")


"""
FILTER

Map does convertion on all objects, filter only filter outs object and does not modify anything

filter(function, iterable) -> same as map
function -> takes an item and returns a boolean. If True its included, if false is skipped
same, lambda is backbone here

Imagine we only want list of rich people who earns >= 80K
"""
rich_people = filter(lambda item: item[3] >= 80000, people)
print(f"Trying to print rich people after filtering\n{rich_people}")
rich_people = list(rich_people)  # same stuff, lazy convert
print(f"Again trying to print rich after filter with list convert\n{rich_people}")
"""
LAMBDA ONLY TAKES EXPRESSION, NOT ANYTHING MORE COMPLEX. IF/ELSE WILL ERROR
# Wrong — statement syntax
lambda item: if item[3] >= 80000 True else False

# Right — ternary expression
lambda item: True if item[3] >= 80000 else False
"""

"""
LIST COMPREHENSION -> Most beloved python feature
map+filter in one go, this is the pythonic way. Avoid MAP/FILTER and avoid 

[expression for item in iterable]              # map only
[item for item in iterable if condition]        # filter only
[expression for item in iterable if condition]  # map + filter
"""

people_rich = [item for item in people if item[3] >= 80000]  # filter
people_compact = [(item[0], item[3]) for item in people]  # map
people_rich_compact = [
    (item[0], item[3]) for item in people if item[3] >= 80000
]  # both
print(rich_people)
print(compact_people)
print(people_rich_compact)
