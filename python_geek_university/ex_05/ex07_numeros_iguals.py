"""
7) Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem
'Números iguais'.
"""
import os as o
import time as t


def MostrarMeiorNum():

    on = True
    while (on == True):
        try:
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))

            if (num1 > num2):
                print(f"{num1} é maior que {num2}")
                on = False
            if (num1 < num2):
                print(f"{num2} é maior que {num1}")
                on = False
            if (num1 == num2):
                print(f"Números iguais")
                on = False
        except Exception as e:
            o.system("cls")
            print(str(e))
            print("Tente informar um número!")


if (__name__ == "__main__"):
    o.system("cls")
    MostrarMeiorNum()
    t.sleep(5)
    o.system("cls")











