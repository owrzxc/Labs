def _get_next_state(pattern, state, char):
    pattern_length = len(pattern)

    if state < pattern_length and char == pattern[state]:
        return state + 1

    for next_state in range(state, 0, -1):
        if pattern[next_state - 1] == char:
            prefix_matched = True

            for i in range(next_state - 1):
                if pattern[i] != pattern[state - next_state + 1 + i]:
                    prefix_matched = False
                    break

            if prefix_matched:
                return next_state

    return 0


def _build_transition_table(pattern):
    alphabet = set(pattern)
    pattern_length = len(pattern)
    transition_table = {}

    for state in range(pattern_length + 1):
        transition_table[state] = {}
        for char in alphabet:
            transition_table[state][char] = _get_next_state(
                pattern, state, char
            )

    return transition_table


def finite_automaton_search(haystack, needle):
    if needle == "":
        return list(range(len(haystack) + 1))

    transition_table = _build_transition_table(needle)
    state = 0
    result = []
    pattern_length = len(needle)

    for index, char in enumerate(haystack):
        if char in transition_table[state]:
            state = transition_table[state][char]
        else:
            state = 0

        if state == pattern_length:
            result.append(index - pattern_length + 1)

    return result


def finite_automaton_search_with_count(haystack, needle):
    indices = finite_automaton_search(haystack, needle)

    return {
        "indices": indices,
        "count": len(indices),
    }