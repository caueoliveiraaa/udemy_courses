"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada do número digitado
"""

num = int(input('Informe um numero: '))

if (num > 0):
    print(f'Ao quadrado {num * num}')
    print(f'Raiz quadrada {num ** 0.5}')
else:
    print(f'{num} é negativo')
