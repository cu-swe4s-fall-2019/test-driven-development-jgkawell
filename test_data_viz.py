import unittest
import data_viz
import random
import os


class TestMathLib(unittest.TestCase):

    def test_boxplot_file_already_exists(self):
        file_name = "test.png"
        f = open(file_name, "w+")
        f.close()

        with self.assertRaises(FileExistsError) as ex:
            data_viz.boxplot([], file_name)

        self.assertEqual(str(ex.exception), "That file name already exists.")

        os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
