from typing import List


def count_paths(grid: List[str]) -> int:
    if not grid:
        return 0

    height = len(grid)
    width = len(grid[0])

    dp = [[0] * width for _ in range(height)]

    for row in range(height):
        dp[row][0] = 1

    same_letter_sum = [0] * 26

    for row in range(height):
        letter_index = ord(grid[row][0]) - ord("a")
        same_letter_sum[letter_index] += dp[row][0]

    for col in range(1, width):
        for row in range(height):
            letter_index = ord(grid[row][col]) - ord("a")
            dp[row][col] = dp[row][col - 1] + same_letter_sum[letter_index]

            if grid[row][col - 1] == grid[row][col]:
                dp[row][col] -= dp[row][col - 1]

        for row in range(height):
            letter_index = ord(grid[row][col]) - ord("a")
            same_letter_sum[letter_index] += dp[row][col]

    if height == 1:
        return dp[0][width - 1]

    return dp[0][width - 1] + dp[height - 1][width - 1]


def solve() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        print(0)
        return

    width = int(data[0])
    height = int(data[1])
    grid = data[2:2 + height]

    if len(grid) != height:
        raise ValueError("Invalid input")

    if any(len(row) != width for row in grid):
        raise ValueError("Invalid row width")

    print(count_paths(grid))


if __name__ == "__main__":
    solve()