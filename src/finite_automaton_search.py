def _get_next_state(pattern: str, state: int, char: str) -> int:
    pattern_length = len(pattern)

    if state < pattern_length and char == pattern[state]:
        return state + 1

    for next_state in range(state, 0, -1):
        if pattern[next_state - 1] != char:
            continue

        prefix_matches = True
        for index in range(next_state - 1):
            if pattern[index] != pattern[state - next_state + 1 + index]:
                prefix_matches = False
                break

        if prefix_matches:
            return next_state

    return 0


def _build_transition_table(pattern: str) -> dict[int, dict[str, int]]:
    alphabet = set(pattern)
    transition_table: dict[int, dict[str, int]] = {}

    for state in range(len(pattern) + 1):
        transition_table[state] = {}
        for char in alphabet:
            transition_table[state][char] = _get_next_state(pattern, state, char)

    return transition_table


def find_all_occurrences(haystack: str, needle: str) -> list[int]:
    if needle == "":
        raise ValueError("needle must not be empty")

    if haystack == "" or len(needle) > len(haystack):
        return []

    transition_table = _build_transition_table(needle)
    state = 0
    result = []

    for index, char in enumerate(haystack):
        state = transition_table.get(state, {}).get(char, 0)
        if state == len(needle):
            result.append(index - len(needle) + 1)

    return result
