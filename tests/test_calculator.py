import unittest
from calculator import suma, resta, multiplicar, dividir


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(0, 4), -4)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertAlmostEqual(dividir(7, 2), 3.5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(1, 0)


if __name__ == '__main__':
    unittest.main()
