from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Tuple


class InvalidMatrixError(ValueError):
    """Raised when the adjacency matrix is invalid."""


def read_adjacency_matrix(file_path: str | Path) -> List[List[int]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    matrix: List[List[int]] = []
    with path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if not row:
                continue
            try:
                matrix.append([int(value.strip()) for value in row])
            except ValueError as exc:
                raise InvalidMatrixError(
                    "Matrix must contain only integer values."
                ) from exc

    validate_adjacency_matrix(matrix)
    return matrix


def validate_adjacency_matrix(matrix: List[List[int]]) -> None:
    if not matrix:
        raise InvalidMatrixError("Matrix must not be empty.")

    size = len(matrix)
    if size > 100:
        raise InvalidMatrixError("Number of islands must be between 1 and 100.")

    for row in matrix:
        if len(row) != size:
            raise InvalidMatrixError("Matrix must be square.")

    for i in range(size):
        if matrix[i][i] != 0:
            raise InvalidMatrixError("Main diagonal must contain zeros.")
        for j in range(size):
            if matrix[i][j] < 0:
                raise InvalidMatrixError("Distances must be non-negative.")
            if matrix[i][j] != matrix[j][i]:
                raise InvalidMatrixError("Matrix must be symmetric.")


def minimum_cable_length(matrix: List[List[int]]) -> int:
    total_length, _ = minimum_cable_plan(matrix)
    return total_length


def minimum_cable_plan(
    matrix: List[List[int]],
) -> Tuple[int, List[Tuple[int, int, int]]]:
    validate_adjacency_matrix(matrix)

    size = len(matrix)
    if size == 1:
        return 0, []

    in_tree = [False] * size
    min_edge = [float("inf")] * size
    parent = [-1] * size
    min_edge[0] = 0
    total_length = 0
    cable_plan: List[Tuple[int, int, int]] = []

    for _ in range(size):
        next_vertex = -1
        next_weight = float("inf")

        for vertex in range(size):
            if not in_tree[vertex] and min_edge[vertex] < next_weight:
                next_weight = min_edge[vertex]
                next_vertex = vertex

        if next_vertex == -1 or next_weight == float("inf"):
            raise InvalidMatrixError("Graph is disconnected.")

        in_tree[next_vertex] = True
        total_length += int(next_weight)

        if parent[next_vertex] != -1:
            cable_plan.append(
                (parent[next_vertex], next_vertex, int(next_weight))
            )

        for neighbor in range(size):
            weight = matrix[next_vertex][neighbor]
            if neighbor == next_vertex:
                continue
            if weight == 0 and not in_tree[neighbor]:
                continue
            if not in_tree[neighbor] and weight < min_edge[neighbor]:
                min_edge[neighbor] = weight
                parent[neighbor] = next_vertex

    return total_length, cable_plan


def solve(file_path: str | Path = "islands.csv") -> int:
    matrix = read_adjacency_matrix(file_path)
    return minimum_cable_length(matrix)


if __name__ == "__main__":
    matrix = read_adjacency_matrix("islands.csv")
    total_length, cable_plan = minimum_cable_plan(matrix)

    print(f"Minimum cable length: {total_length}")
    print("Cable plan:")

    for start, end, distance in cable_plan:
        print(f"{start} -> {end}: {distance}")