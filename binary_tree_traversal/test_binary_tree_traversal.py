from binary_tree_traversal import Node, pre_order, in_order, post_order
from unittest import TestCase


class BinaryTreeTraversalTest(TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def test_pre_order(self):
        expected = [1, 2, 4, 5, 3]
        assert pre_order(self.root) == expected

    def test_in_order(self):
        expected = [4, 2, 5, 1, 3]
        assert in_order(self.root) == expected

    def test_post_order(self):
        expected = [4, 5, 2, 3, 1]
        assert post_order(self.root) == expected
