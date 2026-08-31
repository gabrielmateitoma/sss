import tempfile
import unittest
from pathlib import Path

from p3_path_fixture import resolve_under_root


class TestResolveUnderRoot(unittest.TestCase):
    def test_normal_relative_path(self):
        with tempfile.TemporaryDirectory() as root:
            result = resolve_under_root(root, "safe/file.txt")
            self.assertEqual(result, (Path(root) / "safe/file.txt").resolve())

    def test_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                resolve_under_root(root, "../escape.txt")

    def test_absolute_path_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                resolve_under_root(root, str(Path(root) / "subdir" / ".." / ".." / "escape.txt"))


if __name__ == "__main__":
    unittest.main()
