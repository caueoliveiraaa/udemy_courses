"""
46) Faça um programa que leia um número inteiro positivo de
três digitos (de 100 a 999). Gere outro número formado pelos
dígitos invertidos do número lido. Exemplo:
    NúmeroLido = 123
    NúmeroGerado = 321
"""

num = input('Digite um número inteiror entre 100 e 999: ')

print(f'O número invertido será: {num[::-1]}')
