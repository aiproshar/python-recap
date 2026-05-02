"""
=============================================================================
                        Python Argument Parsing Cheat Sheet
=============================================================================

Module:  argparse (standard library)
Import:  import argparse
Use:     For anything beyond one or two simple values. Handles parsing,
         validation, help text, and error messages automatically.

=============================================================================
                            ARGUMENT TYPES
=============================================================================

1. POSITIONAL ARGUMENTS
   - No dashes, just a name
   - Required by default
   - Order matters — first positional in code = first bare word on CLI

2. OPTIONAL ARGUMENTS (flags / options)
   - Start with - (short) or -- (long)
   - Can provide both:  "-C", "--capitalize"
   - Accessed via the long form name:  args.capitalize
     (if only short form given, accessed via that:  args.C)

=============================================================================
                          ACTION PARAMETER
=============================================================================

action="store"        Default. Grabs the next word and stores it.
                      --output file.txt  →  args.output = "file.txt"

action="store_true"   Boolean flag. No value needed.
                      --verbose  →  args.verbose = True
                      (absent)   →  args.verbose = False

action="store_false"  Opposite boolean flag.
                      --no-cache →  args.no_cache = False

=============================================================================
                          OTHER KEY PARAMETERS
=============================================================================

type=int              Convert the value (default is str).
default="foo"         Value when the argument is not provided.
choices=["a","b"]     Restrict to specific allowed values.
required=True         Make an optional argument mandatory.
help="description"    Text shown in --help output.
nargs="+"             Accept one or more values into a list.
nargs="*"             Accept zero or more values into a list.
nargs="?"             Optional value (uses const if flag present but no value).

=============================================================================
                              EXAMPLE
=============================================================================
"""

import argparse

parser = argparse.ArgumentParser(description="Process and transform a file")

# --- Positional arguments (required, order matters) ---
# usually one or two arguments, for example 'mv src dest'
parser.add_argument("filename")
parser.add_argument("second_filename")

# --- Boolean flag (no value needed) ---
#     -C or --capitalize  →  args.capitalize = True
#     (absent)            →  args.capitalize = False
parser.add_argument("-C", "--capitalize", action="store_true")

# --- Option with a value ---
#     -o result.txt       →  args.output = "result.txt"
#     --output=result.txt →  args.output = "result.txt"
#     (absent)            →  args.output = None
parser.add_argument("-o", "--output")

# --- Parse and use ---


"""
Now how we access all our positional arguments and bool arguments. That's where naming convention comes

=============================================================================
                         NAMING RULES
=============================================================================

  Defined as            Accessed as          Why
  ──────────────────    ─────────────────    ──────────────────────
  "filename"            args.filename        positional → use as-is
  "-C"                  args.C               short only → use letter
  "-C", "--capitalize"  args.capitalize      both → long form wins
  "--output"            args.output          long only → use word
  "--multi-word"        args.multi_word      dashes become underscores
"""
args = parser.parse_args()  # Very first thing, parse first
print(f"First positional :          {args.filename}")
print(f"Second positional:          {args.second_filename}")
print(f"Capitalize bool:            {args.capitalize}")
print(f"Output :                    {args.output}")

"""
=============================================================================
                          USAGE EXAMPLES
=============================================================================

python script.py input.txt data.csv
python script.py input.txt data.csv -C
python script.py input.txt data.csv -C -o result.txt
python script.py input.txt data.csv --capitalize --output=result.txt
python script.py input.txt data.csv -Co result.txt 
python script.py --help
"""

"""
OUTPUTS
(python-recap) arafat@Arafats-MacBook-Pro 004_STANDARD_LIBRARY % python 010_argparse.py input.txt data.csv -Co result.txt 
First positional :          input.txt
Second positional:          data.csv
Capitalize bool:            True
Output :                    result.txt
"""
"""
=============================================================================
                         TYPES OF PARSED VALUES
=============================================================================

The type depends on how you defined the argument, NOT on how you print it.
f-strings hide this by calling str() on everything.

  Defined as                                  args.x type     Example value
  ──────────────────────────────────────────  ──────────────  ─────────────
  add_argument("name")                        str             "input.txt"
  add_argument("count", type=int)             int             42
  add_argument("--verbose", action="store_true")  bool        True
  add_argument("-v", action="count", default=0)   int         3
  add_argument("files", nargs="+")            list[str]       ["a.txt", "b.txt"]
  add_argument("--nums", nargs="+", type=int) list[int]       [1, 2, 3]

Rule: no type= → str. store_true → bool. count → int. nargs → list.
"""
