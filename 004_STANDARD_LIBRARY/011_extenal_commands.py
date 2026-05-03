"""
in GNU/LINUX OS, there are a lot of available command line tools, like
ls, cp, mv, rm, head, tail, aek, sed, grep etc
"""

import subprocess

# just  single command
subprocess.run(["ls"])
result = subprocess.run(["ls"])
print("Return code:", result.returncode)

"""
by default all the outputs are being printed in out terminal, we dont want that
capture_output captures both stdout and stderr
By default its byte stream, text=True makes it string
"""

result = subprocess.run(["pwd"], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error occurred: {result.stdout}")
else:
    print(f'We ran command "pwd", the output: {result.stdout}')

result = subprocess.run(["curl", "https://example.com"], capture_output=True, text=True)
print(result.returncode)  # 0
print(result.stderr)  # still has content (progress output)

"""
The standard way, 90% case to run subprocess
import subprocess

result = subprocess.run(
    ["ls", "-la"],           # command as a list
    capture_output=True,     # capture stdout + stderr
    text=True,               # decode bytes -> str
    check=True               # raise if exit code != 0, need to run with try block
)
print(result.stdout)
print("Return code:", result.returncode)
"""
import subprocess

try:
    result = subprocess.run(
        [
            "kill",
            "1",
        ],  # This will raise permission issue, trying to kill root owned process as user
        capture_output=True,
        text=True,
        check=True,  # raise exception for non-zero exit
    )
except subprocess.CalledProcessError as e:
    # A bit different from previous error print
    # e.__class__.__name__ -> redundant. Always: CalledProcessError
    # e.__str__() / print(e) also not much helpful, prints the command and exit code
    # e.stdout and e.stderr is more useful in subprocess exception
    # It,s a good practice to strip e.stdout and e.stderr, because cli tools of end with extra whitespace and trailing newline
    print(f"subprocess error: {e}:{e.stderr.strip()}")
else:
    # Good example of try else block
    print(result.stdout)
