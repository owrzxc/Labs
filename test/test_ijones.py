import unittest

from src.ijones import count_paths


class TestIJones(unittest.TestCase):
    def test_example_1(self):
        grid = [
            "aaa",
            "cab",
            "def",
        ]
        self.assertEqual(count_paths(grid), 5)

    def test_example_2(self):
        grid = [
            "abcdefaghi",
        ]
        self.assertEqual(count_paths(grid), 2)

    def test_example_3(self):
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
        ]
        self.assertEqual(count_paths(grid), 201684)

    def test_single_cell(self):
        grid = ["a"]
        self.assertEqual(count_paths(grid), 1)

    def test_single_row_no_jumps(self):
        grid = ["abc"]
        self.assertEqual(count_paths(grid), 1)

    def test_single_column(self):
        grid = [
            "a",
            "b",
            "c",
        ]
        self.assertEqual(count_paths(grid), 2)


if __name__ == "__main__":
    unittest.main()