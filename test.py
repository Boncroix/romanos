import unittest
from romanos_fucional import romano_a_entero


class RomanosTest(unittest.TestCase):

    def test_unidades(self):
        # assertEqual compara si es igual  devolvemos el valor de la funcion y lo comparamos contra 1
        self.assertEqual(romano_a_entero('I'), 1)
        self.assertEqual(romano_a_entero('V'), 5)
        self.assertEqual(romano_a_entero('X'), 10)
        self.assertEqual(romano_a_entero('L'), 50)
        self.assertEqual(romano_a_entero('C'), 100)
        self.assertEqual(romano_a_entero('D'), 500)
        self.assertEqual(romano_a_entero('M'), 1000)

    def test_numeros_basicos(self):
        self.assertEqual(romano_a_entero('II'), 2)
        self.assertEqual(romano_a_entero('IV'), 4)
        self.assertEqual(romano_a_entero('IX'), 9)
        self.assertEqual(romano_a_entero('CCV'), 205)
        self.assertEqual(romano_a_entero('MCXXIII'), 1123)

    def test_no_resta_mas_un_orden_de_magnitud(self):
        # asserRaises   error a captar--funcion a ejecutar--parametro de la función la funcion la ejecuta asserRaises
        self.assertRaises(ValueError, romano_a_entero, 'IC')
        self.assertRaises(ValueError, romano_a_entero, 'XM')

    def test_no_restas_consecutivas(self):
        self.assertRaises(ValueError, romano_a_entero, 'IIV')
        self.assertRaises(ValueError, romano_a_entero, 'IVX')
        self.assertRaises(ValueError, romano_a_entero, 'CCM')
        self.assertRaises(ValueError, romano_a_entero, 'IIIIX')
        self.assertRaises(ValueError, romano_a_entero, 'MMCCMM')

    # def test_no_mas_de_tres_simbolos_consecutivos(self):
    #     self.assertRaises(ValueError, romano_a_entero, 'IIII')
    #     self.assertRaises(ValueError, romano_a_entero, 'XIIII')
    #     self.assertRaises(ValueError, romano_a_entero, 'CCCC')

    # def test_no_resta_multiplos_de_cinco(self):
    #     self.assertRaises(ValueError, romano_a_entero, 'VX')
    #     self.assertRaises(ValueError, romano_a_entero, 'VXX')
    #     self.assertRaises(ValueError, romano_a_entero, 'LC')
    #     self.assertRaises(ValueError, romano_a_entero, 'DM')

    def test_otro_caso(self):
        self.assertRaises(ValueError, romano_a_entero, 'XIXXIII')


# TODO: crear un caso de uso para comprobar que el parámentro es una cadena
# TODO: comprobar que el número romano no tiene letras NO VÁLIDAS
# TODO: resolver los dos casos de test comentados arriba (resta múltiplo de 5 y otro caso)
unittest.main()
