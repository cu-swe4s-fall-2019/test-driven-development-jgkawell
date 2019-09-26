import unittest
import math_lib
import random
import math
import statistics


class TestMathLib(unittest.TestCase):

    def test_list_mean_none_list(self):
        result = math_lib.list_mean(None)
        self.assertEqual(result, None)

    def test_list_mean_empty_list(self):
        result = math_lib.list_mean([])
        self.assertEqual(result, None)

    def test_list_mean_int_list(self):
        rand_list = [random.randrange(-1000, 1000) for i in range(1000)]
        result = math_lib.list_mean(rand_list)
        self.assertEqual(result, statistics.mean(rand_list))

    def test_list_mean_double_list(self):
        rand_list = [random.random() for i in range(1000)]
        result = math_lib.list_mean(rand_list)
        self.assertAlmostEqual(result, statistics.mean(rand_list))


if __name__ == '__main__':
    unittest.main()
