import shutil
from pathlib import Path

import shutils

path = Path(__file__).resolve()
file_path = path.parent / "test.txt"
if path.exists():
    print(f"\nThe file {file_path.name} already exists")
else:
    print(f"\nThe file {file_path.name} does not exist")
    print("Let's create a new one, name: test.txt")
    # Write text automatically opens and also closes a file
    file_path.write_text("Hello World")

# File information
print(f"{file_path.name} create time: {file_path.stat().st_ctime}")
# stat_ctime -> creation time
# read_text automatically opens and writes and closes
print(f"{file_path.name} contents: {file_path.read_text()}")


# copying a file
copy_file_path = file_path.parent / "copy.txt"
copy_file_path_another = copy_file_path.parent / "copy_another.txt"
# This is it, we read it and pass the string in to write
copy_file_path.write_text(file_path.read_text())
# also we can copy using shutils to copy
# shutil.copy(source, dest)
shutil.copy(file_path, copy_file_path_another)


print(f"{copy_file_path.name} contents: {copy_file_path.read_text()}")
print(f"{copy_file_path_another.name} contents: {copy_file_path_another.read_text()}")

# cleaning up all files
file_path.unlink()
copy_file_path.unlink()
copy_file_path_another.unlink()
