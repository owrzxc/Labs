import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from finite_automaton_search import find_all_occurrences


class TestFiniteAutomatonSearch(unittest.TestCase):
    def test_multiple_occurrences(self):
        self.assertEqual(find_all_occurrences('ababcabcab', 'abc'), [2, 5])

    def test_overlapping_occurrences(self):
        self.assertEqual(find_all_occurrences('aaaaa', 'aaa'), [0, 1, 2])

    def test_no_occurrences(self):
        self.assertEqual(find_all_occurrences('hello world', 'python'), [])

    def test_pattern_equals_text(self):
        self.assertEqual(find_all_occurrences('needle', 'needle'), [0])

    def test_pattern_longer_than_text(self):
        self.assertEqual(find_all_occurrences('short', 'longerpattern'), [])

    def test_empty_haystack(self):
        self.assertEqual(find_all_occurrences('', 'a'), [])

    def test_empty_needle_raises_error(self):
        with self.assertRaises(ValueError):
            find_all_occurrences('abc', '')


if __name__ == '__main__':
    unittest.main()
