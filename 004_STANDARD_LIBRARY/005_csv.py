"""
CSV manipulation is regularly asked in interview
Also good to export stats from any infra
"""

# Read existing CSV
import csv
import shutil
import time
from pathlib import Path

"""
Sample CSV data (employees.csv):

id  name            department   salary  hire_date   age
1   Alice Johnson   Engineering  75000   2020-03-15  28
2   Bob Smith       Marketing    62000   2019-07-22  34
3   Carol Davis     Engineering  82000   2018-01-10  31
4   David Wilson    Sales        58000   2021-05-03  26
5   Eve Martinez    HR           55000   2017-11-20  42
6   Frank Brown     Engineering  90000   2016-08-14  38
7   Grace Lee       Marketing    67000   2022-02-28  29
8   Henry Taylor    Sales        61000   2020-09-11  33
9   Ivy Chen        Engineering  78000   2021-12-01  27
10  Jack Anderson   HR           59000   2019-04-17  45
"""

# Define the path always, very first step on any
csv_path = Path(__file__).resolve().parent / "employees.csv"

# newline="" is required when using the csv module (both read and write).
# Why: CSV fields can contain embedded newlines inside quoted strings, and
# the csv module needs to handle line endings itself. Without newline="":
#   - On read: embedded \r\n inside quoted fields can get mangled.
#   - On write (Windows): you get \r\r\n at row ends, causing blank lines
#     between every row when opened in Excel.
# Python docs explicitly recommend always passing newline="" with csv.
with open(csv_path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    # next(reader) is the best way to avoid/skip the first row
    next(reader, None)
    for idx, row in enumerate(reader):
        print(f"Line number {idx}: {row[1].upper()}")

# Le's print name , dept and join date for employees who make >= 70K

with open(csv_path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    # next(reader) is the best way to avoid/skip the first row
    next(reader, None)
    for row in reader:
        if int(row[3]) >= 70000:
            print(
                f"Id: {row[0]} Employee: {row[1]} Department: {row[2]} Joined: {row[4]} makes >= 70K"
            )

"""
Lets write a CSV file
"""


#
class Person:
    def __init__(self, name, age, cgpa, major):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.major = major

    def to_list(self):
        return [self.name, self.age, self.cgpa, self.major]


kabir = Person("Kabir Khan", 22, 3.24, "CS")
rifat = Person("Rifat Uddin", 26, 3.42, "ME")


# must use newline even in write
new_csv_path = Path(__file__).resolve().parent / "new.csv"
with open(new_csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "GPA", "MAJOR"])
    """
    csv means comma separated value, everything is converted into string
    Split by commas, so it doesn't matter if you enter inf/float whatever
    """
    writer.writerow(["Arafat", 22, 2.79, "CS"])
    writer.writerow(kabir.to_list())
    writer.writerow(rifat.to_list())
    """
    We can also write to lines in one (Or more)
    writer.writerows([kabir.to_list(), rifat.to_list()])
    """
print("Lets print all the contents of new written csv")

with open(new_csv_path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for rows in reader:
        print(rows)
    print(f"Removing file {new_csv_path.name}")
# It's better to unlink the file outside the with block, as that block lifecycle is tied to opening and read anc close
new_csv_path.unlink()
