import unittest

from src.finite_automaton_search import (
    finite_automaton_search,
    finite_automaton_search_with_count,
)


class TestFiniteAutomatonSearch(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(
            finite_automaton_search("hello world", "world"),
            [6]
        )

    def test_multiple_occurrences(self):
        self.assertEqual(
            finite_automaton_search("ababcabcab", "abc"),
            [2, 5]
        )

    def test_overlapping_occurrences(self):
        self.assertEqual(
            finite_automaton_search("aaaaa", "aa"),
            [0, 1, 2, 3]
        )

    def test_no_occurrence(self):
        self.assertEqual(
            finite_automaton_search("python", "java"),
            []
        )

    def test_empty_needle(self):
        self.assertEqual(
            finite_automaton_search("abc", ""),
            [0, 1, 2, 3]
        )

    def test_empty_haystack(self):
        self.assertEqual(
            finite_automaton_search("", "a"),
            []
        )

    def test_both_empty(self):
        self.assertEqual(
            finite_automaton_search("", ""),
            [0]
        )

    def test_search_with_count_multiple(self):
        self.assertEqual(
            finite_automaton_search_with_count("ababcabcab", "abc"),
            {"indices": [2, 5], "count": 2}
        )

    def test_search_with_count_overlapping(self):
        self.assertEqual(
            finite_automaton_search_with_count("aaaaa", "aa"),
            {"indices": [0, 1, 2, 3], "count": 4}
        )

    def test_search_with_count_no_occurrence(self):
        self.assertEqual(
            finite_automaton_search_with_count("python", "java"),
            {"indices": [], "count": 0}
        )


if __name__ == "__main__":
    unittest.main()