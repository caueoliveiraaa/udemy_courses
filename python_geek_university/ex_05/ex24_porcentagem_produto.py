"""
24) Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%;
SP 12%; RJ %15; MS 8%). Faça um programa que o usuário entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado
não for válido, mostrar uma mensagem de erro.
"""

try:        
    value = int(input("Valor do produdo: "))
    state = input("MG - SP - RJ - MS\nEstado: ")
    if state == 'SP':
        decimal = 12 / 100
        print("SP => 12%\n")
        print(f"Resultado: {value + (value * decimal)}")
    elif state == 'MG':
        decimal = 7 / 100
        print("MG => 12%\n")
        print(f"Resultado: {value + (value * decimal)}")
    elif state == 'RJ':
        decimal = 15 / 100
        print("RJ => 12%\n")
        print(f"Resultado: {value + (value * decimal)}")
    elif state == 'MS':
        decimal = 8 / 100
        print("MS => 12%\n")
        print(f"Resultado: {value + (value * decimal)}")
    else:
        print('Opção inválida')
except Exception as exc:
    print(f"Ocorreu um erro: {exc}")

