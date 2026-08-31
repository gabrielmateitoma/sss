import tempfile
import unittest
from pathlib import Path

from p3_path_fixture import resolve_under_root


class TestResolveUnderRoot(unittest.TestCase):
    def test_normal_relative_path(self):
        with tempfile.TemporaryDirectory() as root:
            result = resolve_under_root(root, "safe/file.txt")
            self.assertEqual(result, (Path(root) / "safe/file.txt").resolve())


if __name__ == "__main__":
    unittest.main()
