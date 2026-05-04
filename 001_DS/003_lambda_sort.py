"""
Anonymous function, why we need it
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
    ["Maria", 31, "Physical Therapist", 82000],
    ["Nick", 63, "Janitor", 32000],
    ["Olivia", 23, "UX Designer", 92000],
]

# We want to sort them based on salary, Descending


def sort_item(item):
    return item[3]


people.sort(key=sort_item, reverse=True)
print("Sorting based on Salary")
print(f"{'Name':<10} {'Age':>3}  {'Profession':<22} {'Salary':>8}")
print("-" * 50)
for p in people:
    print(f"{p[0]:<10} {p[1]:>3}  {p[2]:<22} ${p[3]:>8,}")

"""
This is dumb as fuck, we want to use short lived function, with out defining a one
lambda: simple one line function
lambda:parameter expression (the eval expression is returned)
"""
# Let's sort them, oldest to youngest
# inside sort, x is each item
people.sort(key=lambda x: x[1], reverse=True)
print("\n\nSorting based on Age")
print(f"{'Name':<10} {'Age':>3}  {'Profession':<22} {'Salary':>8}")
print("-" * 50)
for p in people:
    print(f"{p[0]:<10} {p[1]:>3}  {p[2]:<22} ${p[3]:>8,}")


"""
Multi key sort
What if i wanna sort based on age, if age is equal then salary
We can use tuple
minus before a field means descending
We wand descending age and ascending salary in same age
x[1] -> age, x[3] -> salary
"""
people.sort(key=lambda x: (-x[1], x[3]))
print("\n\nSorting based on Descending Age, similar age then ascending salary")
print(f"{'Name':<10} {'Age':>3}  {'Profession':<22} {'Salary':>8}")
print("-" * 50)
for p in people:
    print(f"{p[0]:<10} {p[1]:>3}  {p[2]:<22} ${p[3]:>8,}")
