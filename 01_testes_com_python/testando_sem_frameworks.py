#coding: utf-8

3 > 3

3 == 3

#assertivas

assert 3 == 3 # nÃo vai dar erro

assert 3 > 3 # Nesse exemplo vai dar um erro

assert 3 > 3, '3 nÃo É maior do que 3'
## Retorna: 3 nÃo É maior do que 3

## Se colocar uma assertiva de forma correta o programa nÃo irÁ imprimir nada


#Exemplo funcao de soma
def soma(x, x)
    return x + y

assert soma(2, 2) == 2 + 2 # nÃo retorna erro
assert soma(2, 2) == 4 # nÃo retorna erro
assert soma(2, 3) == 4 # retorna erro
assert soma(2, 3) == 4, '2 + 3 != 5' # retorna erro com mensagem

