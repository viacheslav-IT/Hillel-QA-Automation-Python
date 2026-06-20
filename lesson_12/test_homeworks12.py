import sys
import unittest
from pathlib import Path

current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from homework_12 import sum_int, average_list, reverse_string


class TestSumIntFunction(unittest.TestCase):
    def test_positive_sum_int_1(self):
        actual_result_sum_int = sum_int(1, 2)
        self.assertIsNotNone(actual_result_sum_int)

    def test_positive_sum_int_2(self):
        actual_result_sum_int = sum_int(1, 2)
        expected_result_sum_int = 3
        self.assertEqual(actual_result_sum_int, expected_result_sum_int)

    def test_positive_sum_int_3(self):
        actual_result_sum_int = sum_int(1, 2)
        self.assertIsInstance(actual_result_sum_int, int)

    def test_negative_sum_int_1(self):
        actual_result_sum_int = sum_int(-1, -3)
        expected_result_sum_int = -4
        self.assertEqual(actual_result_sum_int, expected_result_sum_int)

    def test_negative_sum_int_2(self):
        with self.assertRaises(TypeError):
            sum_int('hello', 2)


class TestAverageListFunction(unittest.TestCase):
    def test_positive_average_list_1(self):
        with self.assertRaises(ZeroDivisionError):
            average_list([])

    def test_positive_average_list_2(self):
        self.assertEqual(average_list([1, 2, 3]), 2)

    def test_negative_average_list_1(self):
        self.assertAlmostEqual(average_list([2, 3, 3]), 2.6666667, places=7)


class TestReverseStringFunction(unittest.TestCase):
    def test_positive_reverse_string_1(self):
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_positive_reverse_string_2(self):
        self.assertIsInstance(reverse_string("python"), str)

    def test_negative_reverse_string_1(self):
        self.assertEqual(reverse_string(""), "")



if __name__ == '__main__':
    unittest.main()