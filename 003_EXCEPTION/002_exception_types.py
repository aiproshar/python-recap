"""
in this example we will see that its possible to have more than one exception in a flow, and how we handle them
For example we want to define a function which divides. There can be two exception, first the inputs are not number and second division be zero

Each are different type of exception and must be handled
"""

try:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))
    answer = num_1 / num_2
    print(f"{num_1} divided by {num_2} is: {answer}")
except ZeroDivisionError as e:
    print(f"denominator is zero:", e)
except ValueError as e:
    print(f"value is not a number:", e)


"""
We can also handle multiple exception types on same base exception, because all are inherited from the base exception
"""

try:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))
    answer = num_1 / num_2
    print(f"{num_1} divided by {num_2} is: {answer}")
except Exception as e:
    print("Exception occurred:", e.__class__.__name__, e)

# But this is generally discouraged, you should always catch each type of exception on different block and act accordingly
# Never use baseException, at least use Exception. baseException is too broad
# Another thing, only one except clause is executed, the first matching one. So carefully we can place broader exception at the last
"""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup  (inherits from BaseExceptionGroup + Exception)
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError                (alias: IOError, EnvironmentError)
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError   (3.13+)
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""
