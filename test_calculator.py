import unittest
import calculator


class Testcase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            calculator.divide(6, 0)


if __name__ == "__main__":
    unittest.main()
