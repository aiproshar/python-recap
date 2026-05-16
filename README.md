# python-recap

A hands-on reference and learning repo covering core Python concepts — data structures, OOP, exception handling, and the standard library. Each file is a self-contained runnable example with explanations.

**Python:** 3.12+  **Dependencies:** none (stdlib only)

> **README last synced at commit** [`63bcf8d`](https://github.com/aiproshar/python-recap/commit/63bcf8dfc5d93b0b891b12c01603d4fffdc79d86) _(2026-05-16)_
> Run `git log 63bcf8d..HEAD` to see what's landed since this README was updated.

---

## Sections

### [001_DS](./001_DS/) — Data Structures

| File | Topic |
|------|-------|
| [000_prologue.py](./001_DS/000_prologue.py) | Iterable/sequence/mapping/set hierarchy overview |
| [001_list.py](./001_DS/001_list.py) | List basics — creation, indexing, slicing, type hints |
| [002_list_more.py](./001_DS/002_list_more.py) | Unpacking, enumeration, sort, membership |
| [003_lambda_sort.py](./001_DS/003_lambda_sort.py) | Lambda expressions, multi-key sorting |
| [004_map_filter_comprehension.py](./001_DS/004_map_filter_comprehension.py) | `map`, `filter`, list comprehensions |
| [005_deque.py](./001_DS/005_deque.py) | `collections.deque` — O(1) append/pop on both ends |
| [006_tuple.py](./001_DS/006_tuple.py) | Tuples, named tuples, hashability, unpacking |
| [007_set_dict.py](./001_DS/007_set_dict.py) | Dicts, `defaultdict`, sets, set operations |
| [008_heap.py](./001_DS/008_heap.py) | `heapq` — min-heap operations, max-heap via negation |
| [009_string.py](./001_DS/009_string.py) | String immutability, common methods, interview prep |
| [010_counter.py](./001_DS/010_counter.py) | `collections.Counter` *(WIP)* |

---

### [002_OOP](./002_OOP/) — Object-Oriented Programming

| File | Topic |
|------|-------|
| [001_basic_class.py](./002_OOP/001_basic_class.py) | Class definition, `__init__`, `__str__`, `isinstance` |
| [002_class_method.py](./002_OOP/002_class_method.py) | Class vs instance attributes, `@classmethod`, factory methods |
| [003_magic_method.py](./002_OOP/003_magic_method.py) | Dunder methods — `__eq__`, `__hash__`, `__add__`, `__slots__`, context managers |
| [004_custom_container.py](./002_OOP/004_custom_container.py) | Custom container protocol — `__len__`, `__iter__` *(WIP)* |
| [005_private_mangling.py](./002_OOP/005_private_mangling.py) | Name mangling (`__attr`), single vs double underscore |
| [006_property.py](./002_OOP/006_property.py) | `@property`, setters, deleters, validation |
| [007_inheritance.py](./002_OOP/007_inheritance.py) | Single inheritance, `super()`, MRO, C3 linearization |
| [008_abstract.py](./002_OOP/008_abstract.py) | `ABC`, `@abstractmethod`, enforcing interfaces |
| [009_polymorphism.py](./002_OOP/009_polymorphism.py) | Formal polymorphism vs duck typing |
| [010_static_method.py](./002_OOP/010_static_method.py) | `@staticmethod` — when and why, vs classmethod |

---

### [003_EXCEPTION](./003_EXCEPTION/) — Exception Handling

| File | Topic |
|------|-------|
| [001_basic_exception.py](./003_EXCEPTION/001_basic_exception.py) | `try`/`except`, `ValueError`, exception as control flow |
| [002_exception_types.py](./003_EXCEPTION/002_exception_types.py) | Full exception hierarchy, multiple `except` blocks |
| [003_else_finally.py](./003_EXCEPTION/003_else_finally.py) | `else` and `finally` clauses, return propagation |
| [004_raise_exception.py](./003_EXCEPTION/004_raise_exception.py) | `raise`, choosing exception types, propagating errors |

---

### [004_STANDARD_LIBRARY](./004_STANDARD_LIBRARY/) — Standard Library

| File | Topic |
|------|-------|
| [001_absolu_rel_path.py](./004_STANDARD_LIBRARY/001_absolu_rel_path.py) | `pathlib.Path`, `__file__`, absolute vs relative paths |
| [002_dir_ops.py](./004_STANDARD_LIBRARY/002_dir_ops.py) | `mkdir`, `iterdir`, `rmdir`, `shutil.rmtree` |
| [003_file_ops.py](./004_STANDARD_LIBRARY/003_file_ops.py) | Read, write, copy, stat, unlink |
| [004_zip.py](./004_STANDARD_LIBRARY/004_zip.py) | Creating and extracting zip archives |
| [005_csv.py](./004_STANDARD_LIBRARY/005_csv.py) | `csv.reader` / `csv.writer`, header skipping |
| [006_json.py](./004_STANDARD_LIBRARY/006_json.py) | `json.loads`, type conversion, nested access, `pprint` |
| [007_time_date.py](./004_STANDARD_LIBRARY/007_time_date.py) | `time`, `datetime`, `timedelta`, timezone-aware datetimes |
| [008_random.py](./004_STANDARD_LIBRARY/008_random.py) | `random`, weighted choices, password generation |
| [009_command_argument.py](./004_STANDARD_LIBRARY/009_command_argument.py) | `sys.argv`, positional/optional args, flag conventions |
| [010_argparse.py](./004_STANDARD_LIBRARY/010_argparse.py) | `argparse` — types, defaults, choices, `nargs`, `store_true` |
| [011_extenal_commands.py](./004_STANDARD_LIBRARY/011_extenal_commands.py) | `subprocess.run`, capture output, error handling |

---

### [999_EXTRAS](./999_EXTRAS/) — Extras & Gotchas

Short notes on things that have tripped me up — captured for future reference.

| File | Topic |
|------|-------|
| [001_inv_range.py](./999_EXTRAS/001_inv_range.py) | Iterating a list in reverse with `range(n-2, -1, -1)` |
| [002_infinity.py](./999_EXTRAS/002_infinity.py) | `float('inf')` / `float('-inf')` as min/max sentinels |
| [003_range_index.py](./999_EXTRAS/003_range_index.py) | `range(i, i+k)` element counting in sliding windows |
| [004_is_vs_eq.py](./999_EXTRAS/004_is_vs_eq.py) | `is` vs `==` — identity vs equality |
| [005_floor_ceil_trunc.py](./999_EXTRAS/005_floor_ceil_trunc.py) | `floor`, `ceil`, `trunc`, `//` — rounding direction with negatives |

---

## Running examples

```bash
# run any file directly
python 001_DS/007_set_dict.py

# or with uv
uv run 002_OOP/009_polymorphism.py
```

## Status

| Section | Files | Status |
|---------|-------|--------|
| Data Structures | 11 | `010_counter.py` WIP |
| OOP | 10 | `004_custom_container.py` WIP |
| Exception Handling | 4 | Complete |
| Standard Library | 11 | Complete |
| Modules | — | Planned |
| Extras | 5 | Ongoing — grows as new gotchas come up |
