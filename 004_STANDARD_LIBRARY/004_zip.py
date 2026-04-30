"""
Simple read a zip file, write into a zip file
Or zip a file

"""

import shutil
from pathlib import Path

# Create a zipfile, lets create a temp folder with 5 files
path = Path(__file__).resolve()
temp_dir = path.parent / "temp"
temp_dir.mkdir(parents=True, exist_ok=True)

for i in range(5):
    file = temp_dir / f"{i + 1}.txt"
    file.write_text(f'"Hello World from file {i + 1}.txt"')

# Zip all 5 files into a single archive
# Lets define zip_path, the first important pf any file ops, define the path (the object may or may not exist that comes later)
import zipfile

zip_path = path.parent / "temp.zip"

with zipfile.ZipFile(zip_path, "w") as zip_file:
    for file in temp_dir.iterdir():
        if file.is_file():
            # first parameter: file path, second parameter: the name it will be stored in zip
            # If you don't pass that, they will use the full path name as file name , its messy AF
            zip_file.write(file, file.name, zipfile.ZIP_DEFLATED)

unzip_dir = path.parent / "unzip"
# It's good to open files as read-only
with zipfile.ZipFile(zip_path, "r") as zip_file:
    zip_file.extractall(unzip_dir)
for file in unzip_dir.iterdir():
    print(f"unzipped {file.name} contains: {file.read_text()}")


zip_path.unlink()
shutil.rmtree(unzip_dir)

# TODO: lets use shutils to zip easily, and we can also zip recursively easily, zipping a directory
