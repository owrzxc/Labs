import unittest
from zigzag import zigzag_diagonal_traverse, checksum_first_L_numbers, check_checksum


class TestZigzagDiagonalTraverse(unittest.TestCase):
    def test_5x5(self):
        m = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            1,
            2, 6,
            11, 7, 3,
            4, 8, 12, 16,
            21, 17, 13, 9, 5,
            10, 14, 18, 22,
            23, 19, 15,
            20, 24,
            25,
        ]
        self.assertEqual(zigzag_diagonal_traverse(m), expected)

    def test_2x4(self):
        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag_diagonal_traverse(m), expected)

    def test_6x1(self):
        m = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_diagonal_traverse(m), expected)

    def test_1x1(self):
        m = [[42]]
        expected = [42]
        self.assertEqual(zigzag_diagonal_traverse(m), expected)

    def test_3x3(self):
        m = [
            [1, 2, 5],
            [7, 6, 2],
            [4, 9, 3]
        ]
        expected = [1, 2, 7, 4, 6, 5, 2, 9, 3]
        self.assertEqual(zigzag_diagonal_traverse(m), expected)

    def test_3x3_checksum(self):
        m = [
            [1, 2, 5],
            [7, 6, 2],
            [4, 9, 3]
        ]
        self.assertEqual(checksum_first_L_numbers(m, 4), 14)

        calc, ok = check_checksum(m, 4, 14)
        self.assertEqual(calc, 14)
        self.assertTrue(ok)

        calc, ok = check_checksum(m, 4, 15)
        self.assertEqual(calc, 14)
        self.assertFalse(ok)


if __name__ == "__main__":
    unittest.main()
