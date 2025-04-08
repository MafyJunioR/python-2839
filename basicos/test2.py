import unittest
from test2_funciones import *

class TestFunciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(5, sumar(2, 3))
        self.assertEqual(4, sumar(6, -2))
        self.assertAlmostEqual(0.3, sumar(0.1, 0.2))
    
    def test_dividir(self):
        self.assertEqual(3, dividir(6, 2))

        with self.assertRaises(ZeroDivisionError):
            dividir(7, 0)

unittest.main()  # Calling from the command line invokes all tests