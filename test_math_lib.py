import unittest
import math_lib
import random
import math
import statistics


class TestMathLib(unittest.TestCase):

    """ MEAN TESTS """

    def test_list_mean_none_list(self):
        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(None)

        self.assertEqual(
            str(ex.exception), "List cannot be \'None\'.")

    def test_list_mean_empty_list(self):
        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean([])

        self.assertEqual(
            str(ex.exception), "List cannot be empty.")

    def test_list_mean_int_list(self):
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        result = math_lib.list_mean(rand_int_list)
        self.assertEqual(result, statistics.mean(rand_int_list))

    def test_list_mean_double_list(self):
        rand_double_list = [random.random() for i in range(1000)]
        result = math_lib.list_mean(rand_double_list)
        self.assertAlmostEqual(result, statistics.mean(rand_double_list))

    def test_list_mean_int_and_double_list(self):
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        rand_double_list = [random.random() for i in range(1000)]
        full_list = rand_int_list + rand_double_list
        result = math_lib.list_mean(full_list)
        self.assertAlmostEqual(result, statistics.mean(full_list))

    def test_list_mean_non_num_in_list(self):
        non_num_list = [random.random() for i in range(1000)]
        non_num_list.append("non_num")

        with self.assertRaises(TypeError) as ex:
            math_lib.list_mean(non_num_list)

        self.assertEqual(
            str(ex.exception), "List must only contain numeric values.")

    """ STDEV TESTS """

    def test_list_stdev_none_list(self):
        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev(None)

        self.assertEqual(
            str(ex.exception), "List cannot be \'None\'.")

    def test_list_stdev_empty_list(self):
        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev([])

        self.assertEqual(
            str(ex.exception), "List cannot be empty.")

    def test_list_stdev_int_list(self):
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        result = math_lib.list_stdev(rand_int_list)
        self.assertAlmostEqual(result, statistics.pstdev(rand_int_list))

    def test_list_stdev_double_list(self):
        rand_double_list = [random.random() for i in range(1000)]
        result = math_lib.list_stdev(rand_double_list)
        self.assertAlmostEqual(result, statistics.pstdev(rand_double_list))

    def test_list_stdev_int_and_double_list(self):
        rand_int_list = [random.randrange(-1000, 1000) for i in range(1000)]
        rand_double_list = [random.random() for i in range(1000)]
        full_list = rand_int_list + rand_double_list
        result = math_lib.list_stdev(full_list)
        self.assertAlmostEqual(result, statistics.pstdev(full_list))

    def test_list_stdev_non_num_in_list(self):
        non_num_list = [random.random() for i in range(1000)]
        non_num_list.append("non_num")

        with self.assertRaises(TypeError) as ex:
            math_lib.list_stdev(non_num_list)

        self.assertEqual(
            str(ex.exception), "List must only contain numeric values.")


if __name__ == '__main__':
    unittest.main()
