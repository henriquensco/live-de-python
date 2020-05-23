#coding: utf-8
from operator import add
from unittest import TestCase, main

# para comparar: add(5, 5)

"""string = 'Henrique'

assert string == '.Henrique', 'String errada'
"""

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

"""
# teste da soma
assert soma(5, 5) == add(5, 5)

# teste da sub
assert sub(5, 5) == -1, 'Erro no resultado de sub: {}'.format(sub(5, 5))

#teste da mul
assert mul(3, 3) == 7
"""

def eh_par(val):
	"""
	FunçÃo que verifica se o nÚmero É par.
	
	Arg:
		- val: Valor de entrada do tipo inteiro
	"""
	
	"""
	try:
		return True if val % 2 == 0 else False
	except TypeError:
		return False
	"""
	if isinstance(val, int) or isinstance(val, float):
		return True if val % 2 == 0 else False
	else:
		return False

class Testes(TestCase):
    """def test_soma(self):
    	self.assertEqual(soma(5, 5), 10)
    	#self.assertLess(soma(5, 5), 11)
    	
    def test_soma_errada(self):
    	self.assertEqual(soma(5, 5), 11)
    	
    def test_sub(self):
    	self.assertEqual(sub(5, 5), 0)"""
    
    def test_par(self):
    	self.assertEqual(eh_par(2), True)
    	
    def test_impar(self):
    	self.assertEqual(eh_par(3), False)
    	
    def test_string(self):
    	self.assertEqual(eh_par('string'), False)
    
    def test_float(self):
    	self.assertEqual(eh_par(1.0), False)

if __name__ == '__main__':
    main()
