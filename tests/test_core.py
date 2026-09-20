"""Tests for :mod:`truncate.core`."""

import unittest

from truncate.core import truncate


class TruncateTests(unittest.TestCase):
    def test_short_text_is_unchanged(self):
        self.assertEqual(truncate("hello", 10), "hello")

    def test_exact_limit_is_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_cut_at_word_boundary(self):
        self.assertEqual(truncate("hello brave world", 13), "hello brave")

    def test_cut_before_space_not_after(self):
        # The space after "hello" is at index 5; limit 7 falls inside "brave".
        # The cut must retreat to index 5, giving "hello".
        self.assertEqual(truncate("hello brave world", 7), "hello")

    def test_multiple_spaces(self):
        self.assertEqual(truncate("a   b   c", 6), "a   b")

    def test_whitespace_before_limit(self):
        # Last whitespace at or before 7 is the newline at index 5.
        self.assertEqual(truncate("hello\nworld", 7), "hello")

    def test_no_whitespace_in_window(self):
        # No safe boundary, so a hard cut at the limit is the only option.
        self.assertEqual(truncate("abcdefghij", 3), "abc")

    def test_limit_zero(self):
        self.assertEqual(truncate("hello", 0), "")

    def test_negative_limit(self):
        self.assertEqual(truncate("hello", -5), "")

    def test_empty_string(self):
        self.assertEqual(truncate("", 10), "")

    def test_empty_string_zero_limit(self):
        self.assertEqual(truncate("", 0), "")

    def test_trailing_whitespace_removed(self):
        # The cut lands after "hello" and before two spaces.  rstrip removes
        # those spaces so the result is just "hello".
        self.assertEqual(truncate("hello  world", 7), "hello")


if __name__ == "__main__":
    unittest.main()
