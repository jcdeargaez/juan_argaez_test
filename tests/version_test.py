import unittest

import version


class TestVersion(unittest.TestCase):
    def test_equal_versions(self):
        va = '11.12-a'
        vb = '11.12-a'
        self.assertEqual(version.compare_versions(va, vb), 0)

    def test_numeric_versions(self):
        va = '11.11'
        vb = '12'
        self.assertEqual(version.compare_versions(va, vb), 1)
        self.assertEqual(version.compare_versions(vb, va), -1)

    def test_alfanumeric_versions(self):
        va = '11.11a'
        vb = '11.11b'
        self.assertEqual(version.compare_versions(va, vb), 1)
        self.assertEqual(version.compare_versions(vb, va), -1)

    def test_same_root_different_length(self):
        va = '5.3.7-arch1'
        vb = '5.3.7-arch1-1-ARCH'
        self.assertEqual(version.compare_versions(va, vb), 1)
        self.assertEqual(version.compare_versions(vb, va), -1)

    def test_none_versions(self):
        self.assertEqual(version.compare_versions(None, '1'), 1)
        self.assertEqual(version.compare_versions('1', None), -1)
        self.assertEqual(version.compare_versions(None, None), 0)

    def test_extract_version_parts(self):
        v = '5.3.7-arch1'
        p = [('5', True), ('3', True), ('7', True), ('arch1', False)]
        self.assertListEqual(list(version.extract_version_parts(v)), p)
