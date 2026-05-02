"""
Sometimes we want to run some code if there is no exception thrown
We can think of writing this outside the block, but that will be executed always
"""

try:
    file = open("file.txt", "r")
except PermissionError as e:
    print(f"Permission error: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
# Two except clause also does not guarantee us that we will catch every case
# There can be case where we will have uncaught exception, not being caught by any previous except clause
else:
    # Else block runs if there is no caught/uncaught exception (important: we may still have uncaught exception)
    # We can use broader Exception clause if we want to caught exception any means
    print(f"File {file.name} was opened")
    print(f"Content of file {file.name} is: {file.read()}")
    file.close()


"""
what if we want a cleanup code ? incase of both exception is handled and not handled. Or no exception at all

There can be cases where our exception doesn't cover all the exception cases, and we encounter exception and crash
The finally clause always runs. That is guaranteed

finally always executes unconditionally — on success, on caught exceptions, on uncaught exceptions, and even when return, break, or continue is used in any other clause.

If an exception was unhandled, it propagates after finally clause executes
"""


def withdraw(balance, amount, tranx_id):
    print(f"\n>>> Withdrawing ${amount} from ${balance}")
    try:
        if amount > balance:
            raise ValueError(
                "Insufficient funds"
            )  # More on next example on how to raise exception
        new_balance = balance - amount
    except ValueError as e:
        print(f"{tranx_id}: failed. Exception occurred: {e}")
        new_balance = balance
    else:
        print(f"{tranx_id} Success! New balance: ${new_balance}")
    finally:
        print(f"Logging transaction: {tranx_id}")

    return new_balance


withdraw(100, 30, "1JSX6E4")
withdraw(100, 300, "1JSX6E4")

# Here our error will propagate and program will crash, but our finally block will work
withdraw(100, "bad_input", "1JSX6E4")
