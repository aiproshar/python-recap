# Dispatch Dict Pattern
# =====================
# Replace if/elif chains with a dict mapping keys -> callables.
# Cleaner, easily extended, and turns control flow into data.


# --- The if/elif version (what we're replacing) ---
# Works, but every new operator means a new branch.


def apply_ifelse(op, x, y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x // y
    else:
        raise ValueError(f"unknown op: {op}")


assert apply_ifelse("+", 2, 3) == 5
assert apply_ifelse("/", 7, 2) == 3


# --- The dispatch-dict version (lambdas) ---
# Same behavior, but the operator is a key — adding one is one line.

OPS_LAMBDA = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}


def apply_dispatch(op, x, y):
    return OPS_LAMBDA[op](x, y)


assert apply_dispatch("+", 2, 3) == 5
assert apply_dispatch("/", 7, 2) == 3


# --- Cleaner: use the operator module ---
# Stdlib already ships these callables. Named, faster than lambdas, no boilerplate.

import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

assert OPS["+"](2, 3) == 5
assert OPS["/"](7, 2) == 3


# --- Worked example: Evaluate Reverse Polish Notation ---
# LeetCode 150. RPN puts the operator AFTER its two operands.
# Algorithm: scan left-to-right, push numbers onto a stack;
# on an operator, pop two, apply, push the result. Final stack has one value.


def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in OPS:
            b = stack.pop()  # second operand was pushed last
            a = stack.pop()
            stack.append(OPS[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]


# ["2","1","+","3","*"]  ->  (2 + 1) * 3  =  9
assert eval_rpn(["2", "1", "+", "3", "*"]) == 9

# ["4","13","5","/","+"]  ->  4 + (13 // 5)  =  4 + 2  =  6
assert eval_rpn(["4", "13", "5", "/", "+"]) == 6

print("all dispatch-dict examples passed")
