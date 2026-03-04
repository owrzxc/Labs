import unittest
from hamsters import max_hamsters


class TestMaxHamsters(unittest.TestCase):
    def test_example1(self):
        S = 7
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamsters(S, hamsters), 2)

    def test_example2(self):
        S = 19
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamsters(S, hamsters), 3)

    def test_example3(self):
        S = 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamsters(S, hamsters), 1)

if __name__ == "__main__":
    unittest.main()
