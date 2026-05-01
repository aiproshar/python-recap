"""
Reading a JSON file
Its bit easier for dynamically typed language
"""
import json
from pathlib import Path
from pprint import pprint

json_path = Path(__file__).resolve().parent / "company.json"

#unline CSV, we can directly use readfile
# Due to delimiter complexity, we cannot use this in csv
data = json_path.read_text()
'''
json.load -> load from file like object
json.loads -> load from a string object
we need to do processing
'''
json_payload = json.loads(data)
# use pprint (pretty print) instead of normal print, built in
pprint(json_payload["companies"][0])

print("Tags of second company")
print(json_payload["companies"][1]["tags"])

"""
============================================================
JSON Types and Python Conversion
============================================================

How Python determines JSON field types:
The json module reads the JSON SYNTAX itself (quotes, brackets,
keywords) and creates the matching native Python type. Values
are NOT all strings — unlike CSV, no manual casting is needed.

------------------------------------------------------------
  JSON syntax    ->  Python type
------------------------------------------------------------
  "hello"        ->  str     (anything in double quotes)
  42             ->  int     (digits, no decimal point)
  3.14           ->  float   (digits with a decimal point)
  1.5e10         ->  float   (scientific notation)
  true           ->  True    (bool)
  false          ->  False   (bool)
  null           ->  None    (NoneType)
  [1, 2, 3]      ->  list    (square brackets)
  {"a": 1}       ->  dict    (curly braces) [JSON INSIDE JSON]

------------------------------------------------------------
The quotes are the critical signal
------------------------------------------------------------
  42      ->  int   (no quotes = number)
  "42"    ->  str   (quoted = string, even though it looks numeric)

  data = json.loads('{"a": 42, "b": "42"}')
  data["a"] + 1   # 43        works
  data["b"] + 1   # TypeError: can't add int to str

------------------------------------------------------------
int vs float is decided by the literal
------------------------------------------------------------
  json.loads("42")      ->  int    (no decimal)
  json.loads("42.0")    ->  float  (decimal present)
  json.loads("4e2")     ->  float  (scientific notation -> float
                                    even though the value is 400)

------------------------------------------------------------
Capitalization matters for booleans/null
------------------------------------------------------------
  Valid JSON:      true     false     null     (lowercase)
  Invalid JSON:    True     False     None     (Python style)
                   TRUE     NULL                (any other case)

  Writing `True` or `None` in a .json file -> JSONDecodeError.

------------------------------------------------------------
Big numbers: Python keeps them precise
------------------------------------------------------------
  json.loads('{"x": 99999999999999999999}')
  # Works -- Python int is arbitrary precision.

"""
# Combined employee count of all the companies
total_employee = 0
for company in json_payload["companies"]:
    employee =  company["employee_count"]
    try:

        # employee = int(employee)
        # Converting is redundant, as per previous comment
        # if this was CSV, yes we had to
        total_employee += employee
    except TypeError as e:
        print("Not int:", e)

print(f"Total employees in all the companies: {total_employee}")


# Let's create a list of all companies which were created in 20th century, and their revenue in a list

names = []
for company in json_payload["companies"]:
    if company["founded"] >= 2000:
        names.append([company["name"], company["annual_revenue_millions"]])
print("List of companies founder in or after 2000 and their revenues")
print(names)

'''

for more nested example, it will be like company["teams"]["HR']["head_count"]
example JSON
{
  "name": "Tech Innovations Inc.",
  "founded": 2010,
  "city": "San Francisco",
  "teams": {
    "Engineering": {
      "head": "Carol Davis",
      "head_count": 45,
      "budget": 2500000,
      "is_hiring": true
    },
    "Marketing": {
      "head": "Bob Smith",
      "head_count": 12,
      "budget": 800000,
      "is_hiring": false
    },
    "Sales": {
      "head": "David Wilson",
      "head_count": 20,
      "budget": 1200000,
      "is_hiring": true
    },
    "HR": {
      "head": "Eve Martinez",
      "head_count": 5,
      "budget": 300000,
      "is_hiring": false
    }
  }
}
'''