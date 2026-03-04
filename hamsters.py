def max_hamsters(S: int, hamsters: list[list[int]]) -> int:
    C = len(hamsters)

    def can_feed(k: int) -> bool:
        if k == 0:
            return True
        needs = [H + G * (k - 1) for (H, G) in hamsters]
        needs.sort()
        return sum(needs[:k]) <= S

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