"""
20) Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimemiro de cada lado de um triângulo é menor do que a soma dos outros dois lados.
    - Chama-se equilátero o triângulo que tem três lados iguais
    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

import os

os.system("cls")
while True:

    try:

        a_side = int(input('Informe o primeiro lado do triângulo: '))
        b_side = int(input('Informe o segundo lado do triângulo: '))
        c_side = int(input('Informe o terceiro lado do triângulo: '))

        if a_side + b_side > c_side and a_side + c_side > b_side and b_side + c_side > a_side:

            if a_side == b_side and c_side == a_side:
                print('O triângulo é equilátero')
                break

            elif a_side == b_side or a_side == c_side or c_side == b_side:
                print('O triângulo é isósceles')
                break

            else:
                print('O triângulo é escaleno')
                break

        else:
            os.system("cls")
            print('Os valores acima não podem ser triângulos!')
    
    except ValueError as v:
        os.system("cls")
        print(f'Erro de valor: {v}\nTente um número válido: ')

    except KeyboardInterrupt:
        os.system("cls")
        print(f'Você forçou o programa a parar!\n')
        quit()

    except Exception as e:
        os.system("cls")
        print(f'Ocorreu um erro inesperado: {e}')
