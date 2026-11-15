import unittest

from Prakt9 import calculate_average_price, delete_car


class TestAveragePrice(unittest.TestCase):
    """TC-20, TC-21, TC-22 з Практичного заняття № 11 (FR-03)."""

    def test_average_of_passenger_cars_ignores_type_case(self):
        # Arrange
        cars = {
            "Toyota Camry": ("легковий", 25000.5),
            "Ford Transit": ("вантажний", 30000.0),
            "BMW X5": ("Легковий", 50000.0),
            "Mazda 3": ("ЛЕГКОВИЙ", 18000.25),
            "Volvo FH": ("вантажний", 90000.0),
        }
        # Act
        result = calculate_average_price(cars, "легковий")
        # Assert
        self.assertEqual(result, 31000.25)

    def test_trucks_are_not_counted_in_average(self):
        cars = {
            "Toyota Camry": ("легковий", 100.0),
            "Volvo FH": ("вантажний", 900.0),
        }
        self.assertEqual(calculate_average_price(cars, "легковий"), 100.0)

    def test_single_passenger_car_average_equals_its_price(self):
        cars = {
            "Toyota Camry": ("легковий", 40000.0),
            "Ford Transit": ("вантажний", 30000.0),
        }
        self.assertEqual(calculate_average_price(cars, "легковий"), 40000.0)

    def test_no_passenger_cars_returns_none(self):
        cars = {
            "MAN TGX": ("вантажний", 70000.0),
            "DAF XF": ("вантажний", 65000.0),
        }
        self.assertEqual(calculate_average_price(cars, "легковий"), None)

    def test_empty_dictionary_returns_none(self):
        self.assertEqual(calculate_average_price({}, "легковий"), None)


class TestDeleteCar(unittest.TestCase):
    """TC-23, TC-24 з Практичного заняття № 11 (FR-04)."""

    def setUp(self):
        self.cars = {
            "BMW X5": ("легковий", 50000.0),
            "Volvo FH": ("вантажний", 90000.0),
        }

    def test_delete_existing_model_returns_true(self):
        self.assertTrue(delete_car(self.cars, "BMW X5"))

    def test_delete_existing_model_removes_record(self):
        delete_car(self.cars, "BMW X5")
        self.assertFalse("BMW X5" in self.cars)

    def test_delete_missing_model_returns_false(self):
        self.assertFalse(delete_car(self.cars, "Lada"))

    def test_delete_missing_model_keeps_records(self):
        delete_car(self.cars, "Lada")
        self.assertEqual(len(self.cars), 2)


if __name__ == "__main__":
    unittest.main()
