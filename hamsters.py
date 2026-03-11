def max_hamsters(S: int, hamsters: list[list[int]]) -> int:
    C = len(hamsters)

    def can_feed(k: int) -> bool:
        if k == 0:
            return True

        needs = [H + G * (k - 1) for H, G in hamsters]
        max_need = max(needs)

        count = [0] * (max_need + 1)
        for v in needs:
            count[v] += 1

        taken = 0
        total = 0
        for value in range(max_need + 1):
            if count[value] == 0:
                continue
            take_here = min(count[value], k - taken)
            total += value * take_here
            taken += take_here
            if taken == k:
                break

        return total <= S

    low, high = 0, C
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_feed(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
