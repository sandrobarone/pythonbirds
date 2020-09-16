"""
Para criar um teste em Python usamos "class"



"MÉTODO" pertence a um objeto
"funcao" .....



"""

import unittest


class TesteFizzBuzz(unittest.TestCase):
	def test_com_10(self):
		entrada = 10
		resultado = fizz_buzz(entrada)
		esperado = [
				"1",
				"fizz",
				"3",
				"fizz",
				"buzz",
				"fizz",
				"7",
				"fizz",
				"9",
				"fizzbuzz",
				]
		self.assertListEqual(esperado, resultado)
