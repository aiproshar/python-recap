"""
One of the most important data structures, and also unique to python3
Ordered Dict -> Dict which also preserves input order with a separate doubly linked list
Internally a hash table + doubly linked list → O(1) average lookup, AND O(1) move/pop from either end.


Difference between dict and ordered dict

popitem(last=True/False) -> Pops the very last (newest insert) (last=True)
                            or the very first (oldest insert) (last=False)

   OrderedDict laid out front (oldest) -> back (newest):

   front                                              back
   OLDEST                                             NEWEST
     |                                                  |
     v                                                  v
   +-------+     +-------+     +-------+     +-------+
   |   a   | --> |   b   | --> |   c   | --> |   d   |
   +-------+     +-------+     +-------+     +-------+
     ^                                          ^
     |                                          |
   popitem(last=False)                  popitem(last=True)
   pops 'a' (oldest)                    pops 'd' (newest, default)

   move_to_end(key, last=True)  -> sends key to the BACK  (mark newest)
   move_to_end(key, last=False) -> sends key to the FRONT (mark oldest)


Gotcha: re-assigning an EXISTING key updates its value but does NOT
        reorder it — it stays wherever it was. Only insertion of a NEW
        key appends to the back. To mark an existing key as newest,
        you must call move_to_end() yourself.

Gotcha: Ordered dict is not sorted, that's a big difference. Its ordered, knows the insertion order thanks to additional data structures used
        For example, c++ map is sorted ordered based on keys, sorted on keys. Python just keeps a record of input order
        Default python stdlib does not support sorted ordered containers, only ordered containers
        That's why all operations are constant time, and not logarithmic (tree)

"""

from collections import OrderedDict
from random import random

# ------------ Creating -----------------

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# From any iterable of pairs, same as dict
od2 = OrderedDict(
    [("x", 10), ("y", 20)]
)  # Or any iterable with a tuple of two elements, first one must be hashable, same as dict
print(od2)

# ----------- move to end ----------------
"""
The most important and the headline feature
move_to_end(key, last=True) -> moves to end of doubly linked list
move_to_end(key, last=False) -> moves to front of doubly linked list

We can also think this off a i touched this key, make this most recent, and also updating a key doesn't trigger this,
so everytime we update a key we need to run this
"""

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("a", last=True)  # a goes to the back
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

od.move_to_end("c", last=False)  # c goes to the front
print(od)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# KeyError if the key is missing — guard it like any dict access
try:
    od.move_to_end("missing")
except KeyError as e:
    print(f"move_to_end on missing key raises: {e}")

# ===========================================================================
# EQUALITY — order matters here, unlike plain dict
# ===========================================================================

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)  # True — plain dict ignores order

o1 = OrderedDict([("a", 1), ("b", 2)])
o2 = OrderedDict([("b", 2), ("a", 1)])
print(o1 == o2)  # False

# ===========================================================================
# QUICK REFERENCE
# ===========================================================================
#
#  Operation               | dict        | OrderedDict
#  ------------------------|-------------|-------------
#  insertion order kept    | yes (3.7+)  | yes
#  move_to_end(key)        | NO          | yes  O(1)
#  move_to_end(.., False)  | NO          | yes  O(1)
#  popitem()  (newest)     | yes         | yes  O(1)
#  popitem(last=False)     | NO          | yes  O(1)  ← oldest
#  == compares order       | NO          | yes
#  underlying DS           | hash table  | hash table + doubly linked list


# Classic LRU implementation
class LRUCache:
    def __init__(self, capacity: int):
        self._cache = OrderedDict()
        self._cap = capacity

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._cache.move_to_end(key)  # mark most-recent
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        self._cache[key] = value
        self._cache.move_to_end(key)  # mark most-recent
        if len(self._cache) > self._cap:
            self._cache.popitem(last=False)  # evict least-recent


# Run the LRU
lru = LRUCache(2)
lru.put(1, 1)  # (1,1)
lru.put(2, 2)  # (1,1) (2,2)
print(lru.get(1))  # (2,2) (1,1)
lru.put(3, 3)  # (1,1) (3,3)
print(lru.get(2))  # evicted already, -1
lru.put(4, 4)  # (3,3) (4,4)
print(lru.get(1))  # evicted already, -1
print(lru.get(3))  # 3
print(lru.get(4))  # 4
