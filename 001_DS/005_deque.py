"""
Similar to list, dynamic array
constant append/pop on both end. On list appentleft/popleft is O(n)
constant random access time
"""

from collections import deque

que = deque()  # []
que.append(3)  # [3]
que.append(4)  # [3, 4]
que.append(5)  # [3, 4, 5]

que.appendleft(2)  # [2, 3, 4, 5]
que.append(7)  # [2, 3, 4, 5, 7]
que.pop()  # [2, 3, 4, 5]
que.popleft()  # [3, 4, 5]

que.clear()  # []
