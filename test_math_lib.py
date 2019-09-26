import unittest
import math_lib


class TestMathLib(unittest.TestCase):

    def test_list_mean_empty_list(self):
        result = math_lib.list_mean(None)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
