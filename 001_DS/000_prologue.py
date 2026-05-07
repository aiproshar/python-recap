"""
Iterable (has __iter__ or __getitem__)
│
├── Sequences (ordered, indexed, sliceable)
│   │
│   ├── Mutable
│   │   ├── list
│   │   ├── bytearray
│   │   └── deque
│   │
│   └── Immutable
│       ├── str
│       ├── tuple
│       ├── bytes
│       └── range
│
├── Mappings (key → value)
│   │
│   ├── dict
│   ├── defaultdict
│   └── OrderedDict
│
├── Sets (unique items, no index, no order)
│   │
│   ├── Mutable
│   │   └── set
│   │
│   └── Immutable
│       └── frozenset
│
└── Lazy Iterables (no index, single pass, computed on demand)
    ├── generators        (x for x in range(10))
    ├── map object        map(fn, iterable)
    ├── filter object     filter(fn, iterable)
    ├── zip object        zip(a, b)
    ├── enumerate object  enumerate(iterable)
    └── file objects      open("file.txt")

Sequences — you can do thing[3], thing[1:5], len(thing), loop multiple times
Mappings — you can do thing["key"], but NOT thing[0] (integer index). Iterable over keys by default
Sets — no indexing at all, no order. You can only ask x in thing. Iterable though, so for item in set works
Lazy iterables — no indexing, no len(), and once you consume them they're gone. That's the big gotcha. Can change state on the fly



Every sequence is an iterable, but every iterable is not a sequence
slice operator works on sequence container, not on all iterables (example: dict, set)
"""
