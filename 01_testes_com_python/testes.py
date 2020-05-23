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

class Testes(TestCase):
    def test_soma(self):
    	self.assertEqual(soma(5, 5), 10)
    	
    """def test_soma_errada(self):
    	self.assertEqual(soma(5, 5), 11)"""
    	
    def test_sub(self):
    	self.assertEqual(sub(5, 5), 0)

if __name__ == '__main__':
    main()
