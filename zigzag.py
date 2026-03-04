def zigzag_diagonal_traverse(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    for d in range(m + n - 1):
        temp = []
        row_start = max(0, d - (n - 1))
        row_end = min(d, m - 1)

        for i in range(row_start, row_end + 1):
            j = d - i
            temp.append(matrix[i][j])

        if d % 2 != 0:
            result.extend(temp)
        else:
            result.extend(reversed(temp))

    return result


def checksum_first_L_numbers(matrix, L):
    zz_list = zigzag_diagonal_traverse(matrix)
    return sum(zz_list[:L])


def check_checksum(matrix, L, given_checksum):
    calc = checksum_first_L_numbers(matrix, L)
    return calc, calc == given_checksum

