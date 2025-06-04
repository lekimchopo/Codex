import unittest
import calculator


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculator.suma(2, 3), 5)
        self.assertEqual(calculator.suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(calculator.resta(10, 5), 5)
        self.assertEqual(calculator.resta(0, 4), -4)

    def test_multiplicar(self):
        self.assertEqual(calculator.multiplicar(3, 4), 12)
        self.assertEqual(calculator.multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(calculator.dividir(10, 2), 5)
        self.assertAlmostEqual(calculator.dividir(7, 2), 3.5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.dividir(1, 0)


if __name__ == '__main__':
    unittest.main()
