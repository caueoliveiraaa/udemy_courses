"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básicas, por exemplo). O suário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""
import os
os.system("cls")

while True:
    try:
        n1 = float(input('informe o primeiro numero: '))
        n2 = float(input('informe o segundo numero: '))

        if n1 > 0 and n2 > 0:

            print('\n1 = (+)\n2 = (-)\n3 = (%)\n4 = (x)\n')
            operacao = int(input('digite operacao: '))

            if operacao == 1:
                print(f'\n{round(n1)} + {round(n2)} = {round(n1 + n2)}\n')
                break
            if operacao == 2:
                print(f'\n{round(n1)} - {round(n2)} = {round(n1 - n2)}\n')
                break
            if operacao == 3:
                print(f'\n{round(n1)} % {round(n2)} = {round(n1 / n2)}\n')
                break
            if operacao == 4:
                print(f'\n{round(n1)} X {round(n2)} = {round(n1 * n2)}\n')
                break
            else:
                print('informe uma operacao valida')
        else:
            os.system("cls")
            print('informe numeros validos')
    except Exception as e:
        os.system("cls")
        print(f'ocorreu um erro: {e}')