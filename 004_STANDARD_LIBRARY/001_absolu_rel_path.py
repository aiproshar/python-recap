"""
Working with files and directories starts with paths. Two things confuse beginners:
where the program *thinks* it is (cwd), and where the script file actually lives (__file__).
They are NOT the same. cwd is wherever the shell was when you ran python3, the script
file could be anywhere on disk. Mixing these up is the classic "why can't it find my file"
bug. We will use pathlib.Path because it's the modern way, os.path still works but reads worse.
"""

from pathlib import Path
import os


# cwd = current working directory, basically the shell's PWD when python3 was launched
# If shell PWD is /Users/arafat/Desktop and we run:
#   python3 /Users/arafat/github/python-recap/004_STANDARD_LIBRARY/files_dirs_path.py
# then Path.cwd() is /Users/arafat/Desktop, NOT where the script lives
cwd_path = Path.cwd()
print(f"cwd_path : {cwd_path}")


# __file__ is the path argument we passed to python3, its just a plain str
# - relative arg  -> cwd + arg, kept literally (the /./ and /../ are NOT cleaned up)
# - absolute arg  -> used as is, cwd is ignored
# Try running the script three different ways and watch this change:
#   python3 files_dirs_path.py            -> .../004_STANDARD_LIBRARY/files_dirs_path.py
#   python3 ./files_dirs_path.py          -> .../004_STANDARD_LIBRARY/./files_dirs_path.py
#   python3 /abs/path/files_dirs_path.py  -> /abs/path/files_dirs_path.py
raw_path = Path(__file__)
print(f"raw      : {raw_path}")


# .resolve() collapses '.', '..', and follows symlinks, gives a clean absolute path
# This is the one we usually want to keep around
absolute_path = Path(__file__).resolve()
print(f"absolute : {absolute_path}")


# Relative path back from the script to wherever the user ran python3 from
# Path.relative_to() only works if the file is INSIDE cwd, otherwise it raises ValueError
# os.path.relpath handles the general case, it will use '..' to walk up if needed
relative_path = os.path.relpath(absolute_path, cwd_path)
print(f"relative : {relative_path}")


# Parent of a path = the directory it lives in
# Super useful when you want to read sibling files without depending on cwd
script_dir = absolute_path.parent
print(f"dir      : {script_dir}")


# path.is_dir(path_variable) -> bool returns true if path is dir
# path.is_file(path_variable) -> similar
