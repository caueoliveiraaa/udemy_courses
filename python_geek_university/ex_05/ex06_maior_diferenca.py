"""
6) Escreva um programa que, dados dois números inteiro, mostre na tela
o maior deles, assim como a diferença existentes entre ambos.
"""

from datetime import datetime
import os as o
import pyautogui as p


def maiorNum():
    o.system('CLS')
    go = True

    while (go == True):
        try:
            n1 = int(input('Informe o primeiro numero: '))
            if ((type(n1) == int) == True):
                if (n1 == 0):
                    o.system('CLS')
                    print('Informe um numero que não seja 0!')
                    continue
                elif (n1 < 0):
                    o.system('CLS')
                    print('Informe um numero positivo!')
                    continue
                else:
                    go2 = True
                    while (go2 == True):
                        n2 = int(input('Informe outro numero: '))
                        if ((type(n2) == int) == True):
                            if (n2 == 0):
                                o.system('CLS')
                                print('Informe outro numero que não seja 0!')
                                continue
                            elif (n2 < 0):
                                o.system('CLS')
                                print('Informe outro numero positivo!')
                                continue
                            else:
                                if (n1 == n2):
                                    o.system('CLS')
                                    print(f'{n1} e {n2} sao iguais!')
                                    print('Informe dois numeros diferentes!')
                                    go2 = False
                                    continue
                                elif (n1 > n2):
                                    o.system('CLS')
                                    print(f'Maior: {n1}\nDiferenca: {n1 - n2}')
                                    now = datetime.now()
                                    print(f'fim: {now.day}\{now.month}\{now.year}')
                                    go2 = False
                                    go = False

                                    cont = 2
                                    while (cont >= 0):
                                        p.sleep(1.5)
                                        print(cont + 1)
                                        cont = cont - 1
                                        p.sleep(1.5)
                                    print('Thank you')
                                    p.sleep(3)

                                    o.system('CLS')
                                    continue
                                elif (n1 < n2):
                                    o.system('CLS')
                                    print(f'Maior: {n2}\nDiferenca: {n2 - n1}')
                                    now = datetime.now()
                                    print(f'fim: {now.day}\{now.month}\{now.year}')
                                    go2 = False
                                    go = False

                                    cont = 2
                                    while (cont >= 0):
                                        p.sleep(1.5)
                                        print(cont + 1)
                                        cont = cont - 1
                                        p.sleep(1.5)
                                    p.sleep(1.5)
                                    print('Thank you!')
                                    p.sleep(4)
                                    
                                    o.system('CLS')
                                    continue
            else:
                o.system('CLS')
                print('Informe um numero real (integer)!')
                continue
        except Exception as e:
            o.system('CLS')
            msg = str(e)
            print(f'{e}')
            print('Tente informar os dados corretamente!')

if (__name__ == '__main__'):
    try:
        maiorNum()
    except Exception as e:
        o.system('CLS')
        msg = str(e)
        print(f'{e}')
