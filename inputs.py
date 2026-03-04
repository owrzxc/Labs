from zigzag import zigzag_diagonal_traverse, checksum_first_L_numbers, check_checksum


def main():
    print("Enter h w:")
    h, w = map(int, input().split())

    print(f"Enter {h * w} integers (matrix row by row):")
    nums = list(map(int, input().split()))

    matrix = []
    idx = 0
    for _ in range(h):
        row = nums[idx:idx + w]
        matrix.append(row)
        idx += w

    print("Enter L (how many elements to sum):")
    L = int(input())

    print("Enter given checksum:")
    given_checksum = int(input())

    print("Zigzag traversal of matrix:")
    zz = zigzag_diagonal_traverse(matrix)
    print(zz)

    print(f"Sum of first {L} elements in zigzag order:")
    calc_sum = checksum_first_L_numbers(matrix, L)
    print(calc_sum)

    print("Same wth checksum:")
    _, ok = check_checksum(matrix, L, given_checksum)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
