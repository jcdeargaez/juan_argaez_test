import unittest

import lines


class TestLines(unittest.TestCase):
    def test_equal_lines(self):
        self.assertTrue(lines.intersect(1, 5, 1, 5))
        self.assertTrue(lines.intersect(5, 1, 5, 1))

    def test_non_overlapped_lines(self):
        self.assertFalse(lines.intersect(1, 5, 8, 10))
        self.assertFalse(lines.intersect(1, 5, 10, 8))
        self.assertFalse(lines.intersect(5, 1, 8, 10))
        self.assertFalse(lines.intersect(5, 1, 10, 8))

        self.assertFalse(lines.intersect(8, 10, 1, 5))
        self.assertFalse(lines.intersect(8, 10, 5, 1))
        self.assertFalse(lines.intersect(10, 8, 1, 5))
        self.assertFalse(lines.intersect(10, 8, 5, 1))

    def test_partly_overlapped_lines(self):
        self.assertTrue(lines.intersect(1, 3, 2, 4))
        self.assertTrue(lines.intersect(1, 3, 4, 2))
        self.assertTrue(lines.intersect(3, 1, 2, 4))
        self.assertTrue(lines.intersect(3, 1, 4, 2))

        self.assertTrue(lines.intersect(2, 4, 1, 3))
        self.assertTrue(lines.intersect(2, 4, 3, 1))
        self.assertTrue(lines.intersect(4, 2, 1, 3))
        self.assertTrue(lines.intersect(4, 2, 3, 1))

    def test_fully_overlapped_lines(self):
        self.assertTrue(lines.intersect(1, 4, 2, 3))
        self.assertTrue(lines.intersect(1, 4, 3, 2))
        self.assertTrue(lines.intersect(4, 1, 2, 3))
        self.assertTrue(lines.intersect(4, 1, 3, 2))

        self.assertTrue(lines.intersect(2, 3, 1, 4))
        self.assertTrue(lines.intersect(2, 3, 4, 1))
        self.assertTrue(lines.intersect(3, 2, 1, 4))
        self.assertTrue(lines.intersect(3, 2, 4, 1))

    def test_dots(self):
        self.assertFalse(lines.intersect(1, 1, 1, 1))
        self.assertFalse(lines.intersect(1, 1, 2, 2))
        self.assertFalse(lines.intersect(2, 2, 1, 1))
