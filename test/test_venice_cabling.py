import tempfile
import unittest
from pathlib import Path

from src.venice_cabling import (
    InvalidMatrixError,
    minimum_cable_length,
    minimum_cable_plan,
    read_adjacency_matrix,
    solve,
    validate_adjacency_matrix,
)


class TestVeniceCabling(unittest.TestCase):
    def test_minimum_cable_length_for_valid_graph(self):
        matrix = [
            [0, 2, 3, 3],
            [2, 0, 4, 5],
            [3, 4, 0, 1],
            [3, 5, 1, 0],
        ]

        result = minimum_cable_length(matrix)

        self.assertEqual(result, 6)

    def test_minimum_cable_plan_for_valid_graph(self):
        matrix = [
            [0, 2, 3, 3],
            [2, 0, 4, 5],
            [3, 4, 0, 1],
            [3, 5, 1, 0],
        ]

        total_length, cable_plan = minimum_cable_plan(matrix)

        self.assertEqual(total_length, 6)
        self.assertEqual(cable_plan, [(0, 1, 2), (0, 2, 3), (2, 3, 1)])

    def test_single_island_returns_zero(self):
        self.assertEqual(minimum_cable_length([[0]]), 0)
        self.assertEqual(minimum_cable_plan([[0]]), (0, []))

    def test_disconnected_graph_raises_error(self):
        matrix = [
            [0, 2, 0],
            [2, 0, 0],
            [0, 0, 0],
        ]

        with self.assertRaises(InvalidMatrixError):
            minimum_cable_length(matrix)

        with self.assertRaises(InvalidMatrixError):
            minimum_cable_plan(matrix)

    def test_non_square_matrix_raises_error(self):
        matrix = [
            [0, 1],
            [1, 0],
            [2, 3],
        ]

        with self.assertRaises(InvalidMatrixError):
            validate_adjacency_matrix(matrix)

    def test_non_symmetric_matrix_raises_error(self):
        matrix = [
            [0, 2, 3],
            [1, 0, 4],
            [3, 4, 0],
        ]

        with self.assertRaises(InvalidMatrixError):
            validate_adjacency_matrix(matrix)

    def test_read_adjacency_matrix_from_csv(self):
        csv_content = "0,1,2\n1,0,3\n2,3,0\n"

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "islands.csv"
            file_path.write_text(csv_content, encoding="utf-8")

            matrix = read_adjacency_matrix(file_path)

        self.assertEqual(matrix, [[0, 1, 2], [1, 0, 3], [2, 3, 0]])

    def test_solve_reads_file_and_returns_result(self):
        csv_content = "0,2,3,3\n2,0,4,5\n3,4,0,1\n3,5,1,0\n"

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "islands.csv"
            file_path.write_text(csv_content, encoding="utf-8")

            result = solve(file_path)

        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()