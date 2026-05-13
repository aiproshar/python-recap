# Python Infinity
# ===============
# float('inf') and float('-inf') are useful as initial values
# when tracking minimums and maximums.


# --- Positive Infinity ---
# Greater than any number. Use to initialize a minimum tracker.

print(float("inf") > 999999999)  # True

min_len = float("inf")
windows = [[1, 2], [1, 2, 3, 4], [1]]

for window in windows:
    if len(window) < min_len:
        min_len = len(window)

print(f"Shortest window: {min_len}")  # 1


# --- Negative Infinity ---
# Less than any number. Use to initialize a maximum tracker.

print(float("-inf") < -999999999)  # True

max_val = float("-inf")
data = [3, -10, 42, 7]

for x in data:
    if x > max_val:
        max_val = x

print(f"Largest value: {max_val}")  # 42
