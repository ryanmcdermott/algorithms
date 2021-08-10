from unittest import TestCase
from floyd_cycle_detect import floyd_cycle_detect, Node


class FloydCycleDetectTest(TestCase):
    def test_cycle_present(self):
        node_four = Node(4)
        node = Node(1, Node(2, Node(3, node_four)))
        node_four.next = node
        assert floyd_cycle_detect(node)

    def test_cycle_absent(self):
        node = Node(1, Node(2, Node(3, Node(4))))
        assert not floyd_cycle_detect(node)
