"""
22) Leia a idade e o tempo de serviço de um trabalhador e escreva
se ele pode ou não se aposentar. As condições para posentadoria são
    - Ter pelo menos 64,
    - Ou ter trabalhado pelo menos 30 anos,
    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""
from datetime import datetime
import os


def main():

    today = datetime.now()
    today_str = today.strftime('%d/%m/%Y %H:%M:%S')
    print('Começou:', today_str)
    
    while True:
        try:
            age = int(input('Informe a idade: '))
            years_of_service = int(input('Informe a quantidade de anos de serviço: '))

            if (age > 0) and (years_of_service > 0) and (years_of_service < age):

                if (age >= 64):
                    print(f'Pode aposentar por ter {age} anos.')
                    today = datetime.now()
                    end = today.strftime('%d/%m/%Y %H:%M:%S')
                    print('Terminou: ', end)
                    break

                elif (years_of_service > 30):
                    print(f'Pode aposentar por ter trabalhado pelo menos {years_of_service} anos.')
                    today = datetime.now()
                    end = today.strftime('%d/%m/%Y %H:%M:%S')
                    print('Terminou: ', end)
                    break

                elif (age >= 60) and (years_of_service > 25):
                    print(f'Pode aposentar por ter {age} anos e ter trabalhado {years_of_service} anos.')
                    today = datetime.now()
                    end = today.strftime('%d/%m/%Y %H:%M:%S')
                    print('Terminou: ', end)
                    break

                else:
                    print(f'Não pode se aposentar com idade {age} e ter trabalhado {years_of_service} anos.')
                    stop = input('Digite "S" para parar ou outro caractere para continuar: ')

                    if (stop.upper() == "S"):
                        today = datetime.now()
                        end = today.strftime('%d/%m/%Y %H:%M:%S')
                        print('Terminou: ', end)
                        break

            elif (years_of_service > age):
                print('Idade deve ser maior que anos de serviço.')

            else:
                print('Informe valores válidos.')

        except KeyboardInterrupt:
            today = datetime.now()
            end = today.strftime('%d/%m/%Y %H:%M:%S')
            print('\nTerminou: ', end)
            print('Progama parado manulamente.')
            break
        
        except Exception as e:
            os.system('cls')
            print(f'\nOcorreu um erro: {e}')
            print('Informe valores válidos.')


if (__name__ == '__main__'):
    os.system('cls')
    main()