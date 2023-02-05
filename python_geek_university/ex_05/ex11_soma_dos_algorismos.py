"""
11) Escreva um programa que leia um número inteiro maior do que zero
e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número
251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que
zero, programa terminará com a mensagem 'Número inválido'
"""
import os as o
import time as t
import pyautogui as p


def func():

    seguir = True
    while seguir:
        try:
            n = int(input("Informe um numero maior que 0: "))
            if (n > 0):
                n = str(n)
                nLst = list(n)

                soma = 0
                for n in nLst:
                    n = int(n)
                    soma += n
                
                display = ''
                for num in nLst:
                    display += f' {num} + '

                print(f'Soma de {display} = {soma}')
                seguir = False
            else:
                print('Informe um numero maior que zero: ')
        except Exception as e:
            print(f"Erro: {str(e)}")
            print('Informe um numero')


if (__name__ == '__main__'):
    o.system('cls')
    func()
