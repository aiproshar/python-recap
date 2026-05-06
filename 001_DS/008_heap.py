"""
Python has default minHeap implementation, works on any DS with random access, ideally list
Operations:
    1. heapify(list): Restore heap property on unorganized list
    2. heappush(list, item): Push and element (append on the list) and restore heap property
    3. heappop: pop the smallest number and return it,  and also restore heap property. Warning: empty heap will throw exception
    4. peak that top: list[0] -> first element is the root

    MAX HEAP: By default, python has ho max heap, lets get smart, use negative numbers, and also invert them after pop
"""

import heapq

heap = [
    1,
    3,
    4,
    5,
    2,
    6,
    7,
    4,
    3,
    7,
    8,
    44,
    33,
]
heapq.heapify(heap)
print(f"Poping smallest element: {heapq.heappop(heap)}")
heapq.heappush(heap, -1)
print(f"Poping smallest element: {heapq.heappop(heap)}")
print(f"Poping second smallest element: {heapq.heappop(heap)}")

# Doing reverse order
print("\n\n\n-------- Max Heap -----------")
nums = [1, 3, 4, 5, 2, 6, 77, 4, 3, 7, 8, 44, 33]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
print(f"Poping Largest element: {heapq.heappop(max_heap) * -1}")
heapq.heappush(
    max_heap, -100
)  # we want to push 100, so before push neg it because it's a max heap
print(f"Poping second largest element: {heapq.heappop(max_heap) * -1}")

"""
HEAP on custom data structure, more precisely, on a tuple, and this one is important
Imagine we need top 5 elements from 1 million stream, sorting the data for only 5 element ? Yikes
And also if its a true stream, you gonna invoke sort on every stream ? More yikes
"""


fruits = [
    {"name": "apple", "count": 5, "expiry": 10},
    {"name": "banana", "count": 3, "expiry": 8},
    {"name": "mango", "count": 5, "expiry": 10},
    {"name": "grape", "count": 3, "expiry": 12},
    {"name": "kiwi", "count": 7, "expiry": 9},
    {"name": "orange", "count": 5, "expiry": 7},
    {"name": "peach", "count": 3, "expiry": 8},
    {"name": "strawberry", "count": 7, "expiry": 9},
]

fruit_heap = [
    (-item["count"], item["expiry"], item["name"]) for item in fruits
]  # item* -1 -> not pythonic -item: pythonic
heapq.heapify(fruit_heap)

while fruit_heap:
    count, expiry, item = heapq.heappop(fruit_heap)
    print(f"{item:>12}  count={count * -1:<4}  expiry={expiry:<4}")


"""
COLLISION: When count AND expiry both match, tuples with dicts would crash
because dicts aren't comparable. Use itertools.count as a unique tiebreaker.
"""
from itertools import count

counter = count()

fruits_with_collision = [
    {"name": "apple", "count": 5, "expiry": 10},
    {"name": "banana", "count": 3, "expiry": 8},
    {"name": "mango", "count": 5, "expiry": 10},  # collides with apple
    {"name": "grape", "count": 3, "expiry": 12},
    {"name": "kiwi", "count": 7, "expiry": 9},
    {"name": "orange", "count": 5, "expiry": 7},
    {"name": "peach", "count": 3, "expiry": 8},  # collides with banana
    {"name": "strawberry", "count": 7, "expiry": 9},  # collides with kiwi
]

# Without counter — this would crash on collision:
# (-5, 10, {"name": "apple"}) vs (-5, 10, {"name": "mango"})
# TypeError: '<' not supported between instances of 'dict' and 'dict'

# Without counter — crashes on collision
try:
    bad_heap = [
        (-item["count"], item["expiry"], item) for item in fruits_with_collision
    ]  # uncomparable
    heapq.heapify(bad_heap)
except TypeError as e:
    print(f"Crashed!, unable to compare dict type: {e}")


# RULE OF THUMB: Python compares the tuple left to right, if first element same, goes to second and moves on
# Will throw error of there is uncomparable type (eg> dict), it will not throw error if no compare left and all previous are same (doesn't care)
# That's why we need a tiebreaker, because if the fields are same we don't care who comes first, we don't want it to go further in tuple


# With counter — comparison never reaches the dict
fruit_heap = [
    (-item["count"], item["expiry"], next(counter), item)
    for item in fruits_with_collision
]
heapq.heapify(fruit_heap)

print("\n\n\n-------- Heap with tiebreaker counter -----------\n")
print(f"{'name':>12}  {'count':<6}  {'expiry':<6}  {'insertion':<6}")
print("-" * 45)

while fruit_heap:
    neg_count, expiry, insertion_order, item = heapq.heappop(fruit_heap)
    print(f"{item['name']:>12}  {neg_count * -1:<6}  {expiry:<6}  {insertion_order:<6}")
