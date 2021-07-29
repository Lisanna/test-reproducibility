"""Test the utility functions."""

import unittest
from template_package.utils import iter_together
import pathlib

HERE = pathlib.Path(__file__).parent.resolve()


class TestUtils(unittest.TestCase):
    """Test the utilities."""

    def test_my_function(self):
        """Test the :func: iter_together."""
        path_1 = HERE.joinpath('test1.txt')
        path_2 = HERE.joinpath('test2.txt')
        results = iter_together(path_1, path_2)
        expected = [
            ('hello', 'goodbye'),
            ('ciao', 'ciao')
        ]
        self.assertEqual(expected, results)