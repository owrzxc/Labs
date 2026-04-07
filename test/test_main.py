import unittest
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from main import BinaryTree, find_successor


def build_example_tree():
    root = BinaryTree(10)
    node5 = BinaryTree(5, parent=root)
    node15 = BinaryTree(15, parent=root)
    root.left = node5
    root.right = node15

    node3 = BinaryTree(3, parent=node5)
    node7 = BinaryTree(7, parent=node5)
    node5.left = node3
    node5.right = node7

    node20 = BinaryTree(20, parent=node15)
    node15.right = node20

    node12 = BinaryTree(12, parent=node20)
    node20.left = node12

    return root, node3, node7, node15, node20


class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        (self.root,
         self.node3,
         self.node7,
         self.node15,
         self.node20) = build_example_tree()

    def test_successor_of_7_is_10(self):
        succ = find_successor(self.root, self.node7)
        self.assertIsNotNone(succ)
        self.assertEqual(succ.value, 10)

    def test_successor_of_10_is_15(self):
        succ = find_successor(self.root, self.root)
        self.assertIsNotNone(succ)
        self.assertEqual(succ.value, 15)

    def test_successor_of_20_is_none(self):
        succ = find_successor(self.root, self.node20)
        self.assertIsNone(succ)


if __name__ == "__main__":
    unittest.main()