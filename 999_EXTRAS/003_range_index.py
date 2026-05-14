# Range Indexing in Sliding Windows
# ==================================
# range(a, b) gives you elements from a up to but NOT including b.
# The count of elements is simply b - a.


# --- Why range(i, i + k) and NOT range(i, i + k + 1) ---
# If you want k elements starting from index i,
# range(i, i + k) already gives exactly k items because range excludes the end.

k = 3
i = 0

print(list(range(i, i + k)))  # [0, 1, 2]     → 3 elements ✅
print(list(range(i, i + k + 1)))  # [0, 1, 2, 3]  → 4 elements ❌ one too many

# The math: range(i, i + k) produces (i + k) - i = k elements. Always.


# --- How many windows fit? ---
# Array of length n, window of size k.
# Last valid window starts at index n - k.
# So we iterate i from 0 to n - k inclusive → range(n - k + 1).

items = [10, 20, 30, 40, 50, 60]
n = len(items)
k = 3

print(f"\nn={n}, k={k}")
print(f"Number of windows: n - k + 1 = {n - k + 1}")

for i in range(n - k + 1):
    window = items[i : i + k]
    print(f"  i={i} → window = {window}")

# i=0 → [10, 20, 30]
# i=1 → [20, 30, 40]
# i=2 → [30, 40, 50]
# i=3 → [40, 50, 60]   ← last window, starts at n - k = 3


# --- Common off-by-one mistakes ---

# WRONG: range(n - k)      → misses the last window
# RIGHT: range(n - k + 1)  → includes the last window

# WRONG: range(i, i + k + 1) → grabs k+1 elements, goes out of bounds on last window
# RIGHT: range(i, i + k)     → grabs exactly k elements


# --- Quick mental trick ---
# range excludes the end, so always ask:
#   "How many elements do I want?" → that's your k
#   "range(start, start + k)" → done, no +1 needed
