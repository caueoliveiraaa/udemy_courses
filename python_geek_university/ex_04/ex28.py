"""
28) Faça a leitura de três valores e apresente como resultado a
soma dos quadrados dos três valores lidos.
"""

num_1 = int(input('Digite o primeiro número: ')) 
num_2 = int(input('Digite o segundo número: ')) 
num_3 = int(input('Digite o terceiro número: '))


num_1 *= num_1
num_2 *= num_2
num_3 *= num_3
res = num_1 + num_2 + num_3


print(f'O resultado da soma dos três números elevados ao quadrado é: {res}')
