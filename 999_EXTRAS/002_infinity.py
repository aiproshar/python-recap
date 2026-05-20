# Python Infinity
# ===============
# float('inf') and float('-inf') are useful as initial values
# update: math.inf and -math.inf much better option
# when tracking minimums and maximums.
import math
from sys import flags

# --- Positive Infinity ---
# Greater than any number. Use to initialize a minimum tracker.

print(math.inf > 999999999999999999)  # True always, add as many 9s as you want

min_len = math.inf
windows = [[1, 2], [1, 2, 3, 4], [1]]

for window in windows:
    if len(window) < min_len:
        min_len = len(window)

print(f"Shortest window: {min_len}")  # 1


# --- Negative Infinity ---
# Less than any number. Use to initialize a maximum tracker.

print(-math.inf < -9999999999999999999)  # True always, add as many 9s as you want

max_val = -math.inf
data = [3, -10, 42, 7]

for x in data:
    if x > max_val:
        max_val = x

print(f"Largest value: {max_val}")  # 42
