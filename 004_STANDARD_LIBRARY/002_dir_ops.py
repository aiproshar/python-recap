from pathlib import Path


# Use resolve, its both uses absolute path and also collapses . and .. and ./ ect
# Absolute only does half work, use resole always
script_path = Path(__file__).resolve()
fake_script_path = script_path.parent / "fake_script.py"
parent_folder = script_path.parent
print(f"script path: {script_path}, exists: {script_path.exists()}")
print(f"fake_script path: {fake_script_path}, exists: {fake_script_path.exists()}")


# Let's make a folder, we already have the parent dir in parent_folder
# parents means we create all the missing directory a/b/c/d/e , only a/b exist then this will create all of them
temp_folder = parent_folder / "temp"
temp_folder.mkdir(parents=True, exist_ok=True)
# Let's make a file on that folder and read it
temp_file = temp_folder / "temp_file.txt"
temp_file.write_text("hello world")
try:
    file = open(temp_file, "r")
    print(f"file opened: {file.name} content: {file.read()}")
except Exception as e:
    print(f"Exception occurred: {e.__class__.__name__}:{e}")
finally:
    file.close()


# Let's create a couple of files and nested dirs on that temp folder, we want to do some iteration

# 5 directories
for i in range(1, 6):
    (temp_folder / f"dir_{i}").mkdir(exist_ok=True)

# 10 files (2 per directory)
for i in range(1, 6):
    for j in range(1, 3):
        f = temp_folder / f"dir_{i}" / f"file_{j}.txt"
        f.write_text(f"hello from dir_{i}/file_{j}")

# 5 files in parent dir
for i in range(1, 6):
    f = temp_folder / f"file_{i}.txt"
    f.write_text(f"hello from file_{i}")

# Item.suffix prints the extension. Empty string for a folder
for item in temp_folder.iterdir():
    print(f"item: {item} Extension:{item.suffix}")

paths = [item for item in temp_folder.iterdir() if item.is_dir()]
print(f"paths: {paths}")
# If we have million of files/dirs use generators
paths = (i for i in temp_folder.iterdir() if i.is_dir())

print("\n\n\nPrinting using generators \n\n\n")
for path in paths:
    print(f"path: {path}")

# Let's delete all the files
# This is done via the unlink method
#
for path in temp_folder.iterdir():
    if not path.is_dir():
        path.unlink()

# Let's print all the items, files should be gone
print("Printing all the items after unlinking files")
for path in temp_folder.iterdir():
    print(f"path: {path}")

# Now lets remove the dirs
for path in temp_folder.iterdir():
    if path.is_dir():
        try:
            path.rmdir()
        except Exception as e:
            print(f"Exception occurred: {e.__class__.__name__}:{e}")

# OOPS, we cannot remove a directory with contents, this is a safety net
# We need to run something like rm -rf {dir} here
import shutil

for path in temp_folder.iterdir():  # noqa: E402
    if path.is_dir():
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"Exception occurred: {e.__class__.__name__}:{e}")

# YaY. we cleaned all the mess. Let's remove the temp folder, we can use normal remove because there is no child here
temp_folder.rmdir()
# Lets run a ls on script dir

print(f"\n\n\nPrinting all the items in {parent_folder.name} \n\n")
# Remember, parent folder is our script path, in this folder our man script lives
for path in parent_folder.resolve().iterdir():
    print(path)
