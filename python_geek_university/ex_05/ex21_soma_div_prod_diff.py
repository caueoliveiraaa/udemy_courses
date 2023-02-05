"""
21) Escreva o menu de opções abaixo. Leia a opção do usuário e
execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 número (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""

import os
import traceback

def main():
    run = True
    while run:
        try:
            
            # Menu
            menu_str = """Escolha a opção:
                1 - Soma de 2 números
                2 - Diferença entre 2 números
                3 - Produto entre 2 números
                4 - Divisão entre 2 números
                => """

            option = input(menu_str)
            if (option == '1'):
                print('Opção => "1 - Soma de 2 números" selecionada!\n')

                get_number = True
                while get_number:
                    try:
                        number1 = int(input('Informe o primeiro numero inteiro: '))
                        number2 = int(input('Informe o segundo numero inteiro: '))

                        if (number1 > 0) and (number2 > 0):
                            print(f'{number1} + {number2} = {number1 + number2}')
                            get_number = False
                            run = False
                            print(f'Programa finalizado.')

                        else:
                            print('Informe numeros maiores que zero!')

                    except KeyboardInterrupt:
                        os.system('cls')
                        get_number = False
                        run = False
                        print('Programa parado manulamente')

                    except Exception:
                        print('\nOcorreu um erro:')
                        print(traceback.format_exc(),'\n')
                        print('Tente informar um número válido!')

            elif (option == '2'):
                print('Opção => "2 - Soma de 2 números" selecionada!\n')

                get_number = True
                while get_number:
                    try:
                        number1 = int(input('Informe o primeiro numero inteiro: '))
                        number2 = int(input('Informe o segundo numero inteiro: '))

                        if (number1 > 0) and (number2 > 0) and (number1 != number2):
                            if (number1 > number2):
                                print(f'Diferença entre {number1} e {number2} = {number1 - number2}')
                                get_number = False
                                run = False
                                print(f'Programa finalizado.')

                            elif (number2 > number1):
                                print(f'Diferença entre {number2} e {number1} = {number2 - number1}')
                                get_number = False
                                run = False
                                print(f'Programa finalizado.')

                        elif (number1 == number1):
                            print('Para saber a diferença dos números eles precisam ser diferentes.')

                        else:
                            print('Informe numeros maiores que zero.')

                    except KeyboardInterrupt:
                        os.system('cls')
                        get_number = False
                        run = False
                        print('Programa parado manulamente')

                    except:
                        print('\nOcorreu um erro:')
                        print(traceback.format_exc())
                        print('Tente informar um número válido.')

            elif option == '3':
                print('Opção => "3 - Produto entre 2 números" selecionada!\n')

                get_number = True
                while get_number:
                    try:
                        number1 = int(input('Informe o primeiro numero inteiro: '))
                        number2 = int(input('Informe o segundo numero inteiro: '))

                        if (number1 > 0) and (number2 > 0):
                            print(f'{number1} X {number2} = {number1 * number2}')
                            get_number = False
                            run = False
                            print(f'Programa finalizado.')

                        else:
                            print('Informe numeros maiores que zero.')

                    except KeyboardInterrupt:
                        os.system('cls')
                        get_number = False
                        run = False
                        print('Programa parado manulamente')

                    except:
                        print('\nOcorreu um erro:')
                        print(traceback.format_exc())
                        print('Tente informar números válidos.')

            elif option == '4':
                print('Opção => "4 - Divisão entre 2 números" selecionada!\n')

                get_number = True
                while get_number:
                    try:
                        number1 = int(input('Informe o primeiro numero inteiro: '))
                        number2 = int(input('Informe o segundo numero inteiro: '))

                        try:
                            print(f'{number1} % {number2} = {(number1 / number2)}')
                            get_number = False
                            run = False
                            print(f'Programa finalizado.')

                        except ZeroDivisionError:
                            print(f'Erro de divisão:')
                            print(traceback.format_exc())
                            print('Tente informar númeors diferentes de 0.')

                        except KeyboardInterrupt:
                            os.system('cls')
                            get_number = False
                            run = False
                            print('Programa parado manulamente.')

                        except Exception:
                            print('Ocorreu um erro:')
                            print(traceback.format_exc())
                            print('Tente informar números válidos.')
                    except:
                        print('Ocorreu um erro:')
                        print(traceback.format_exc())
                        print('Tente informar números válidos.')

            else:
                os.system('cls')
                print("Informe uma opção válida.")

        except KeyboardInterrupt:
            os.system('cls')
            get_number = False
            run = False
            print('Programa parado manulamente.')

        except Exception:
            os.system('cls')
            print('Ocorreu um erro:')
            print(traceback.format_exc())
            print('Tente informar números válidos.')


if (__name__ == '__main__'):
    os.system('cls')
    main()
