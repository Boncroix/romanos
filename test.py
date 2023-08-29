import unittest
from romanos_v01 import RomanNumber


class RomanosTest(unittest.TestCase):
    def test_crear_numero_romano_desde_entero(self):
        numero = RomanNumber(1)
        self.assertEqual(numero.valor, 1)
        self.assertEqual(numero.cadena, 'I')
        numero = RomanNumber(1745)
        self.assertEqual(numero.valor, 1745)
        self.assertEqual(numero.cadena, 'MDCCXLV')

    def text_crear_numero_romano_desde_cadena(self):
        cadena = RomanNumber('I')
        self.assertEqual(cadena.valor, 1)
        self.assertEqual(cadena.cadena, 'I')
        cadena = RomanNumber('MDCCXLV')
        self.assertEqual(cadena.valor, 1745)
        self.assertEqual(cadena.cadena, 'MDCCXLV')


unittest.main()
