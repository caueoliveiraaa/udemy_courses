"""
12) Leu um número inteiro. Se o número lido for negativo, escreva a mensagem
'Número inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
import math

n = int(input('informe um numero: '))

if n > 0:
    print(f'logaritmo: {math.log(n)}')
else:
    print('numero invalido')    

