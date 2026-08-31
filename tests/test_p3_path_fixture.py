import tempfile
import unittest
from pathlib import Path

from p3_path_fixture import resolve_under_root


class TestResolveUnderRoot(unittest.TestCase):
    def test_normal_relative_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = resolve_under_root(tmp, "subdir/file.txt")
            self.assertTrue(str(result).startswith(tmp))


if __name__ == "__main__":
    unittest.main()
