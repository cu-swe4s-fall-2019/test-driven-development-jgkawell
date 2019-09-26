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
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        result = math_lib.list_mean(rand_int_list)
        self.assertEqual(result, statistics.mean(rand_int_list))

    def test_list_mean_double_list(self):
        rand_double_list = [random.random() for i in range(1000)]
        result = math_lib.list_mean(rand_double_list)
        self.assertAlmostEqual(result, statistics.mean(rand_double_list))

    def test_list_mean_non_num_in_list(self):
        non_num_list = [random.random() for i in range(1000)]
        non_num_list.append("non_num")

        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean(non_num_list)

        self.assertEqual(
            str(ex.exception), "List must only contain numeric values.")


if __name__ == '__main__':
    unittest.main()
