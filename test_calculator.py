import unittest
import calculator


class Testcase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(2, -3), -1)
        self.assertEqual(calculator.add(-2, -3), -5)
        self.assertEqual(calculator.add(2, 0), 2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(3, 2), 1)
        self.assertEqual(calculator.subtract(3, -2), 5)
        self.assertEqual(calculator.subtract(-3, -2), -1)
        self.assertEqual(calculator.subtract(3, 0), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(2, -3), -6)
        self.assertEqual(calculator.multiply(-2, -3), 6)
        self.assertEqual(calculator.multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(6, -3), -2)
        self.assertEqual(calculator.divide(-6, -3), 2)
        self.assertEqual(calculator.divide(6, 1), 6)


if __name__ == '__main__':
    unittest.main()
