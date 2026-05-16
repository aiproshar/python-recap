"""
FLOOR, CEIL, TRUNCATE, and //
==============================
These all convert a float to an int, but they disagree on DIRECTION.

Floor    → round toward -∞ (always go LEFT on number line)
Ceil     → round toward +∞ (always go RIGHT on number line)
Truncate → round toward 0  (chop the decimal, shrink toward zero)
//       → floor division  (divide then floor). Same as floor for division results.

They all agree on positive numbers. The difference shows up with NEGATIVES.
"""

import math

# ===========================================================================
# POSITIVE NUMBERS — all three "rounding" directions agree
# ===========================================================================

x = 7.7
print(f"math.floor(7.7)  = {math.floor(x)}")  # 7  ← toward -∞
print(f"math.ceil(7.7)   = {math.ceil(x)}")  # 8  ← toward +∞
print(f"math.trunc(7.7)  = {math.trunc(x)}")  # 7  ← toward 0
print(f"int(7.7)         = {int(x)}")  # 7  ← same as trunc

# ===========================================================================
# NEGATIVE NUMBERS — here they DISAGREE, this is the interview gotcha
# ===========================================================================

x = -7.7
print(f"math.floor(-7.7) = {math.floor(x)}")  # -8 ← toward -∞ (goes MORE negative)
print(f"math.ceil(-7.7)  = {math.ceil(x)}")  # -7 ← toward +∞ (goes LESS negative)
print(f"math.trunc(-7.7) = {math.trunc(x)}")  # -7 ← toward 0  (chops decimal)
print(f"int(-7.7)        = {int(x)}")  # -7 ← same as trunc

# ===========================================================================
# // (FLOOR DIVISION) — divide, then FLOOR the result
# ===========================================================================
#
# a // b  is equivalent to  math.floor(a / b)
# NOT math.trunc(a / b). This matters for negatives.

print(f" 13 //  5 = {13 // 5}")  #  2  ← 13/5 = 2.6,  floor(2.6) = 2
print(f"-13 //  5 = {-13 // 5}")  # -3  ← -13/5 = -2.6, floor(-2.6) = -3  ← NOT -2!
print(f" 13 // -5 = {13 // -5}")  # -3  ← same logic
print(f"-13 // -5 = {-13 // -5}")  #  2  ← -13/-5 = 2.6, floor(2.6) = 2

# If you WANT truncation toward zero (like C/Java), use int() on true division:
print(f"int(-13 / 5) = {int(-13 / 5)}")  # -2 ← truncate, not floor

# ===========================================================================
# VISUAL: number line for -7.7
# ===========================================================================
#
#   -8        -7        0         7         8
#    |---------|---------|---------|---------|
#         ^
#       -7.7 sits here
#
#   floor(-7.7) = -8   ← go LEFT  toward -∞
#   ceil(-7.7)  = -7   ← go RIGHT toward +∞
#   trunc(-7.7) = -7   ← go toward 0 (RIGHT in this case, because -7 is closer to 0)
#
# For positive 7.7:
#   floor(7.7) = 7     ← go LEFT  toward -∞
#   ceil(7.7)  = 8     ← go RIGHT toward +∞
#   trunc(7.7) = 7     ← go toward 0 (LEFT in this case)
#
# See the pattern? trunc and floor agree on positives, trunc and ceil agree on negatives.

# ===========================================================================
# QUICK REFERENCE
# ===========================================================================
#
#  Value  | floor | ceil | trunc | //  (as x // 1)
#  -------|-------|------|-------|------
#   2.6   |   2  |   3  |   2  |   2
#  -2.6   |  -3  |  -2  |  -2  |  -3
#   7.0   |   7  |   7  |   7  |   7
#  -7.0   |  -7  |  -7  |  -7  |  -7
#
# Rule of thumb:
#   floor = toward -∞ (always)
#   ceil  = toward +∞ (always)
#   trunc = toward  0 (always)
#   //    = floor division (divide then floor)
#   int() on a float = trunc
