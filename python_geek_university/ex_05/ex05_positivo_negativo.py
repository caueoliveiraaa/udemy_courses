"""
5) Faça um programa que receba um número inteiro e verifique se este número é
par ou ímpar.
"""
import os as o
import time as t


o.system('cls')
seguir = True
while seguir:
    try:
        num = input('"s" para sair\nInforme um numero: ')
        
        if (num == 's') or (num == 'S'):
            seguir = False
        else:
            num = int(num)
            if (num % 2) == 0:
                o.system('cls')
                print(f'{num} é par')
            else: 
                o.system('cls')
                print(f'{num} é impar')
    except:
        o.system('cls')
        print('Informe o número corretamente!')