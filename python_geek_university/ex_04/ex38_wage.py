"""
38) Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""

sal = float(input('Informe o salário: '))
aumento = 25.0 / 100.0
novo_sal = sal + (aumento * sal)
print(f'O novo salário será: {novo_sal}')
