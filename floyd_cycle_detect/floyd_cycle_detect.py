class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def floyd_cycle_detect(node):
    slow = node
    fast = node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
