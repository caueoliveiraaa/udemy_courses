"""
8) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas
e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente,
um valor entre 0.0 e 10.0.
"""
import os as o
import time as t


def AverageGrades():

    seguir = True
    while seguir:

        try:
            n1 = int(input('Informe a primeira nota: '))
            n2 = int(input('Informe a segunda nota: '))

            if (type(n1) == int) and (type(n2) == int) and (n1 >= 0) and (n1 <= 10) and (n2 >= 0) and (n2 <= 10):
                print(f'A média das duas notas é {(n1 + n2) / 2}')
            
            sair = input('Deseja sair? "sim"/"não":')

            sair = sair.lower()
            if (sair == "sim"):
                seguir = False            
                print('fim')
            elif (sair == "não") or (sair == "nao"):
                seguir = False 
                print('fim')
            else:
                print('Dados inválidos')           

        except Exception as e:
            o.system('cls')
            print(f"Erro: {str(e)}")


if (__name__ == '__main__'):
    o.system('cls')
    AverageGrades()