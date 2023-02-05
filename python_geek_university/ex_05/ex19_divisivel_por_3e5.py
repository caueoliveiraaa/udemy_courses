"""
19) Faça um programa para verificar se um determinado número
inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""
import os

os.system("cls")
while True:

    try:

        num = int(input('Informe um número: '))

        if (num % 3 == 0) and (num % 5 == 0):
            print(f'O número {num} é divisível por 3 e 5!')

        elif (num % 5 == 0):
            print(f'O número {num} é divisível por 5 e não é por 3!')

        elif (num % 3 == 0):
            print(f'O número {num} é divisível por 3 e não é por 5!')

        else:
            print(f'O número {num} não é divisível nem por 3 e nem por 5')
        
        stop = input('Digite E para sair ou qualquer outro charactere para continuar: ')
        stop = stop.lower()
        if stop == 'e':
            os.system("cls")
            break
        else:
            os.system("cls")
    
    except ValueError as v:
        os.system("cls")
        print(f'Erro de valor: {v}\nTente um número válido: ')

    except Exception as e:
        os.system("cls")
        print(f'Ocorreu um erro inesperado: {e}')

    except KeyboardInterrupt:
        os.system("cls")
        print(f'Você forçou o programa a parar!\n')
        quit()