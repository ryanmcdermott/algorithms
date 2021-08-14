class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root):
    res = []

    def traverse(node):
        if not node:
            return

        res.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return res


def in_order(root):
    res = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)
    return res


def post_order(root):
    res = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        res.append(node.val)

    traverse(root)
    return res
