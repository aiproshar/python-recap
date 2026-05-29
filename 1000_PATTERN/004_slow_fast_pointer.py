"""
Floyd's cycle detection algorithm in a linked list
Slow pointer and Fast pointer, be extra careful not to do None dereference
Another pass is needed if we want to find the exact node where collision  happens
"""


class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val


head = Node()
slow = head
fast = head

# Fast is always ahead, we need to save him from None dereference
while fast and fast.next:
    # Slow one jump
    slow = slow.next

    # Fast two jump
    fast = fast.next
    fast = fast.next

    # Loop invariant: we do jumps and compare, that's how we avoid initial compare on start node
    if slow == fast:
        # Return True
        pass

"""
How we find the exact node where the cycle was created ?

Create a third pointer from head, move slow pointer and third pointer by one node each iteration
THey will meet in the collision point
"""
# THis is a conditional block below, only of we found a cycle we run the cycle start find, and that's why we're not doing
# Dereference checks anymore


another = head

# Cycle exists, now find the start
while another is not slow:
    slow = slow.next
    another = another.next
# We exited, means we in the node where loop created
# Return another
