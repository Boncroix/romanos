import unittest
from romanos import romano_a_entero


class RomanosTest(unittest.TestCase):

    def test_unidades(self):
        self.assertEqual(romano_a_entero('I'), 1)
        self.assertEqual(romano_a_entero('V'), 5)
        self.assertEqual(romano_a_entero('X'), 10)
        self.assertEqual(romano_a_entero('L'), 50)
        self.assertEqual(romano_a_entero('C'), 100)
        self.assertEqual(romano_a_entero('L'), 500)
        self.assertEqual(romano_a_entero('M'), 1000)


unittest.main()
