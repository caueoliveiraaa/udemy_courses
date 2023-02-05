"""
10) Faça um porgrama que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as sequintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""
import os as o
import time as t
import pyautogui as p


def func():

    seguir = True
    while seguir:

        try:
            alt = float(input("Informe a altura: "))
            sx = input("h = homen\nm = mulher\nInforme o sexo: ")
            sx = sx.lower()

            if sx == "h":
                print(f"Peso ideal masculino: {(72.7 * alt) - 58}")
                seguir = False
            if sx == "m":
                print(f"Peso ideal feminino: {(62.1 * alt) - 58}")
                seguir = False
        
        except Exception as e:
            print(f"Erro: {str(e)}")
            print('Tente informar os dados corretamente')


if (__name__ == '__main__'):
    o.system('cls')
    func()