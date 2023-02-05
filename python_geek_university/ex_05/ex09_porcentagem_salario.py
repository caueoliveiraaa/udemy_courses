"""
9) Leia o salário de um trabalhador e o valor da prestação
de um empréstimo. Se a prestação for maior que 20% do salário imprima:
'Empréstimo não concedido', caso contrário imprima: 'Empréstimo concedido'
"""
import os as o
import time as t


def func():

    seguir = True
    while seguir:

        try:
            salario = float(input("Informe o salário do trabalhador: "))
            prestacao = float(input("Informe o valor das prestações do empréstimo: "))

            if (prestacao > salario * 0.2):
                print("Empréstimo não concedido")
            else:
                print("Empréstimo concedido")
                
            break

        except Exception as e:
            print(f"Erro: {str(e)}")
            print("Informe os dados corretamente!")


if (__name__ == '__main__'):
    o.system('cls')
    func()