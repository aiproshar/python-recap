"""
Command line argument are important things, they change the behaviour of the program during run time
For example you can also provide db credentials, ports ect
sys.argv -> a list of all the arguments, the first argument is always the file_name
So even if we don't provide any argument, we have sys.argv[0] -> the file name
Please run this file like python3 004_STANDARD_LIBRARY/009_command_argument.py first_arg second_arg
sys.argv doesn't interpret anything. It just gives you a raw list of strings, split by spaces.
Each item in sys.argv is a string, we need to convert this first
you can give python3 file.py -n kube-system --parallel=100 it will see list["-n", "kube-system", "--parallel=100"]
You need a parser to parse arguments (described below)

"""

import sys


print(sys.argv)

if len(sys.argv) == 1:
    print("You didn't supply any argument(s)")
    print(f"File name: {sys.argv[0]}")
else:
    print(f"You supplied {len(sys.argv) - 1} argument(s)")
    print(f"File name: {sys.argv[0]}")
    print(f"Other Params: {sys.argv[1:]}")  # all real arguments

"""
Types of argument
------ Positional Argument ---------
python script.py hello world
                 ↑     ↑
              arg 1   arg 2



----------- short flags/options --------------

Part of original unix system
single dash single letter, example: -v -vv -x
python script.py -v -o output.txt -n 5
Some are just flags, some are options. so shorts can be two types: flags and options (flags wih values)
options that take values always space separated
We can combine two three flags. For example: python3 script.py -x -c -f as python3 script.py -xcf
-xcf will be broken down to -x -c -f
anti-pattern: grep -n=5 (don't use equal on short options as separator, always space for short forms)

while combine two three flags, last value can be options
python3 script.py -vfo file.txt
#                 ││└─ needs value → grabs "file.txt"
#                 │└── flag ✓
#                 └─── flag ✓
this works because the command line argument will be broken down to "python3 script.py -v -f -o file.txt"


------------ long flags/options ----------------

Double dash, full word. More readable, self documenting
It was not part of original unix, brought by GNU extension
can be both flag and options. Options can be defined as two ways, space separated and using equal(=)
examples:
        python3 script.py --output=a.txt
        python3 script.py --output a.txt
        python3 script.py --verbose --serialize --output=a.txt
                                               
                                               
But be aware, system.argv will see two args using space separation, one using "="



------------------------------ TLDR---------------------------------
# POSIX style (short only)
ls -l -a -h
ls -lah
cp -r src/ dest/

# GNU style (short + long)
grep -i --color=auto pattern file
tar -xvf archive.tar --directory=/tmp
curl -o output.html --silent --max-time=30

The GNU guideline is:

Short options use a space: -o value
Long options can use either: --output value or --output=value
= is never used with short options in standard tools

"""


"""
---------------------------------  Argument Parsing  ----------------------------------
import argparse -> the standard python argument parsing tool
For anything beyond one or two simple values, argparse is the way to go. It handles parsing, validation, help text, and error messages
"""
