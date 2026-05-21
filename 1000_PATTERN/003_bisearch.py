"""
=============================================================================
              Binary Search — Three Core Templates
=============================================================================

Binary search runs in O(log n). The tricky part is never the idea —
it's getting the loop condition, boundary updates, and return value
exactly right. There are three patterns that cover almost everything.

We'll use ONE example array throughout all three templates:

  nums = [1, 3, 5, 5, 5, 7, 9]
  index:  0  1  2  3  4  5  6

  target = 5  (appears at indices 2, 3, 4)

This lets you clearly see how each template behaves differently
on the exact same input.

=============================================================================
                    TEMPLATE 1 — EXACT MATCH
=============================================================================

Goal:   Find ANY index of a specific target value.
        Return -1 if not found.

Key features:
  - Loop condition:  lo <= hi   (search space can shrink to one element)
  - Three branches:  ==, <, >
  - Both bounds exclude mid:  lo = mid + 1,  hi = mid - 1
  - Early return on match

When to use:
  - "Find target in sorted array"
  - "Return index of X"
  - Any time you need the position of a known value
"""


def binary_search_exact(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid  # found it, done
        elif nums[mid] < target:
            lo = mid + 1  # target is to the right, exclude mid
        else:
            hi = mid - 1  # target is to the left, exclude mid

    return -1  # exhausted search space, not found


# --- Quick test ---
nums = [1, 3, 5, 5, 5, 7, 9]
result = binary_search_exact(nums, 5)
print(result)


"""
=============================================================================
                 TEMPLATE 2 — LEFT BOUND (find minimum)
=============================================================================

Goal:   Find the LEFTMOST (smallest) index that satisfies a condition.
        Classic use: first occurrence of target in sorted array.

Key features:
  - Loop condition:  lo < hi    (strict! converges when lo == hi)
  - Two branches only, NO early return
  - "Condition met"  →  hi = mid     (mid might be answer, keep it)
  - "Condition not met"  →  lo = mid + 1  (mid is definitely bad, skip it)
  - Return lo (or hi, they're equal when loop ends)

Why hi = mid and not mid - 1?
  Because mid MIGHT be the answer. Setting hi = mid - 1 could
  exclude the correct result. We keep it in the search space.

Why lo < hi and not lo <= hi?
  With hi = mid, using lo <= hi would infinite-loop when lo == hi == mid.
  lo < hi naturally terminates at the convergence point.
"""


def binary_search_left_bound(nums: list[int], target: int) -> int:
    """Return index of first occurrence of target, or -1 if not found."""
    lo = 0
    hi = len(nums)  # NOTE: hi = len(nums), not len(nums) - 1
    # We use len(nums) so that if every element is < target,
    # lo converges to len(nums), meaning "not found / insert at end"

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] >= target:  # condition met: mid could be the answer
            hi = mid
        else:  # nums[mid] < target: too small, skip
            lo = mid + 1

    # lo == hi now. Check if we actually found the target.
    if lo < len(nums) and nums[lo] == target:
        return lo
    return -1


nums = [1, 3, 5, 5, 5, 7, 9]
print(binary_search_left_bound(nums, 5))
"""
=============================================================================
                TEMPLATE 3 — RIGHT BOUND (find maximum)
=============================================================================

Goal:   Find the RIGHTMOST (largest) index that satisfies a condition.
        Classic use: last occurrence of target in sorted array.

Key features:
  - Loop condition:  lo < hi    (strict, same as left bound)
  - Two branches only, NO early return
  - "Condition met"  →  lo = mid      (mid might be answer, keep it)
  - "Condition not met"  →  hi = mid - 1  (mid is definitely bad, skip it)
  - mid = (lo + hi + 1) // 2         ← CRITICAL: round UP to avoid infinite loop
  - Return lo (or hi, they're equal when loop ends)

Why round up?
  When lo + 1 == hi and condition is met, lo = mid.
  If mid = (lo + hi) // 2 = lo (rounds down), then lo = lo → infinite loop!
  Rounding up: mid = (lo + hi + 1) // 2 = hi, so lo = hi → loop ends.

  This is the #1 gotcha of the right bound template.

Trace with nums = [1, 3, 5, 5, 5, 7, 9], target = 5:

  [1, 3, 5, 5, 5, 7, 9]
   0  1  2  3  4  5  6

  Step 1:  lo=0  hi=6  mid=(0+6+1)//2=3  nums[3]=5 <= 5? YES  → lo=3
  Step 2:  lo=3  hi=6  mid=(3+6+1)//2=5  nums[5]=7 <= 5? NO   → hi=4
  Step 3:  lo=3  hi=4  mid=(3+4+1)//2=4  nums[4]=5 <= 5? YES  → lo=4
  Step 4:  lo=4  hi=4  → loop ends, lo == hi == 4

  Result: index 4, the LAST 5.  ✓

  Notice step 1: we found a 5 at index 3 but did NOT return.
  We set lo=3 and kept searching right. Mirror image of left bound.

  Notice step 3: if we had used (3+4)//2 = 3 (round down),
  lo = 3 again → infinite loop. The +1 saved us.
"""


def binary_search_right_bound(nums: list[int], target: int) -> int:
    """Return index of last occurrence of target, or -1 if not found."""
    if not nums:
        return -1

    lo = 0
    hi = len(nums) - 1

    while lo < hi:
        mid = (lo + hi + 1) // 2  # round UP to prevent infinite loop

        if nums[mid] <= target:  # condition met: mid could be the answer
            lo = mid
        else:  # nums[mid] > target: too big, skip
            hi = mid - 1

    # lo == hi now. Check if we actually found the target.
    if nums[lo] == target:
        return lo
    return -1


nums = [1, 3, 5, 5, 5, 7, 9]
binary_search_right_bound(nums, 5)  # last 5


"""
=============================================================================
              ALL THREE ON THE SAME INPUT — COMPARISON
=============================================================================

  nums = [1, 3, 5, 5, 5, 7, 9],  target = 5

  Template 1 (exact):       returns 3  (any 5 — happened to land on middle one)
  Template 2 (left bound):  returns 2  (first 5)
  Template 3 (right bound): returns 4  (last 5)

  Same array, same target, three different answers.
  The templates differ in what they do when they FIND a match:

    exact:        return immediately
    left bound:   keep searching LEFT   (hi = mid)
    right bound:  keep searching RIGHT  (lo = mid, with mid rounded up)


=============================================================================
                         CHEAT SHEET SUMMARY
=============================================================================

  Template        Loop         mid formula          On match         On miss         Return
  ──────────────  ───────────  ───────────────────  ───────────────  ──────────────  ──────
  Exact match     lo <= hi     (lo + hi) // 2       return mid       lo=mid+1 or     -1
                                                                     hi=mid-1

  Left bound      lo < hi      (lo + hi) // 2       hi = mid         lo = mid + 1    lo
  (find min)

  Right bound     lo < hi      (lo + hi + 1) // 2   lo = mid         hi = mid - 1    lo
  (find max)               ↑ round up!


=============================================================================
                       DECISION GUIDE
=============================================================================

Ask yourself:

  1. Am I looking for a specific value?
     → Template 1 (exact match)

  2. Am I looking for the SMALLEST value satisfying a condition?
     → Template 2 (left bound)
     → hi = mid (keep mid, search left)
     → mid rounds down (default)

  3. Am I looking for the LARGEST value satisfying a condition?
     → Template 3 (right bound)
     → lo = mid (keep mid, search right)
     → mid rounds UP (add +1 before dividing)


=============================================================================
                       COMMON PITFALLS
=============================================================================

  1. Off-by-one in hi initialization
     - Exact match:  hi = len(nums) - 1
     - Left bound:   hi = len(nums) or len(nums) - 1 depending on problem
     - Right bound:  hi = len(nums) - 1

  2. Forgetting to round up in right bound
     → Infinite loop when lo + 1 == hi

  3. Using lo <= hi with hi = mid
     → Infinite loop when lo == hi == mid

  4. Early return in left/right bound templates
     → Skips the actual minimum/maximum, returns first match found instead

  5. Wrong branch grouping
     → For left bound:  "meets condition" and "equals target" are the SAME branch
        (both shrink hi). The == case is NOT special.
"""
