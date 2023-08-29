import unittest
from romanos import RomanNumber


class RomanosTest(unittest.TestCase):
    def test_crear_numero_romano_desde_entero(self):
        numero = RomanNumber(1)
        self.assertEqual(numero.valor, 1)
        self.assertEqual(numero.cadena, 'I')
        numero = RomanNumber(1745)
        self.assertEqual(numero.valor, 1745)
        self.assertEqual(numero.cadena, 'MDCCXLV')

    def test_crear_numero_romano_desde_cadena(self):
        cadena = RomanNumber('I')
        self.assertEqual(cadena.valor, 1)
        self.assertEqual(cadena.cadena, 'I')
        cadena = RomanNumber('MDCCXLV')
        self.assertEqual(cadena.valor, 1745)
        self.assertEqual(cadena.cadena, 'MDCCXLV')

    def test_numero_romano_tiene_representacion_de_cadena(self):
        numero = RomanNumber(1745)
        self.assertEqual(str(numero), 'MDCCXLV')

    def test_comprobar_igualdad(self):
        numero = RomanNumber(1)
        numerouno = RomanNumber(1)
        numerodos = RomanNumber(2)
        self.assertEqual(numero, numerouno)
        self.assertNotEqual(numero, numerodos)
        self.assertNotEqual(numerouno, numerodos)

    def test_comprobar_suma(self):
        numero = RomanNumber(1)
        numerouno = RomanNumber(2)
        self.assertEqual(numero + numerouno, 3)
        self.assertEqual(numero + 'VII', 8)


unittest.main()
