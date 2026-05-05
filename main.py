from collections import deque


def read_input(filename="input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    start = tuple(map(int, lines[0].split(",")))
    end = tuple(map(int, lines[1].split(",")))
    rows, cols = map(int, lines[2].split(","))

    matrix = []
    for i in range(3, 3 + rows):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    return start, end, matrix, rows, cols


def bfs_shortest_path(matrix, start, end, rows, cols):
    sx, sy = start
    ex, ey = end

    if not (0 <= sx < rows and 0 <= sy < cols and 0 <= ex < rows and 0 <= ey < cols):
        return -1

    if matrix[sx][sy] == 0 or matrix[ex][ey] == 0:
        return -1

    visited = [[False] * cols for _ in range(rows)]
    queue = deque()

    queue.append((sx, sy, 0))
    visited[sx][sy] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (ex, ey):
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1


def write_output(result, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(result))


def main():
    start, end, matrix, rows, cols = read_input()
    result = bfs_shortest_path(matrix, start, end, rows, cols)
    write_output(result)


if __name__ == "__main__":
    main()