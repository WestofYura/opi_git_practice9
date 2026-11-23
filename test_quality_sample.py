import unittest
from contextlib import redirect_stdout
from io import StringIO

from quality_sample import calculate_order_total

ITEMS = [{"price": 500, "qty": 1}, {"price": 250, "qty": 2}]


class TestCalculateOrderTotal(unittest.TestCase):
    def test_student_gets_discount(self):
        self.assertEqual(calculate_order_total(ITEMS, "student"), 900)

    def test_teacher_gets_discount(self):
        self.assertEqual(calculate_order_total(ITEMS, "teacher"), 900)

    def test_guest_has_no_discount(self):
        self.assertEqual(calculate_order_total(ITEMS, "guest"), 1000)

    def test_empty_order_total_is_zero(self):
        self.assertEqual(calculate_order_total([], "student"), 0)

    def test_debug_mode_prints_total(self):
        output = StringIO()
        with redirect_stdout(output):
            calculate_order_total(ITEMS, "student", debug=True)
        self.assertEqual(output.getvalue().strip(), "Calculated total: 900.0")


if __name__ == "__main__":
    unittest.main()
