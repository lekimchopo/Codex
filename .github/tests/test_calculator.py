import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.suma(2, 3), 5)
        self.assertEqual(calculadora.suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(calculadora.resta(10, 5), 5)
        self.assertEqual(calculadora.resta(0, 4), -4)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(3, 4), 12)
        self.assertEqual(calculadora.multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(10, 2), 5)
        self.assertAlmostEqual(calculadora.dividir(7, 2), 3.5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(1, 0)


if __name__ == '__main__':
    unittest.main()
