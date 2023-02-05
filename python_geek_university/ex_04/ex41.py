"""
41) Faça um programa que leia o valor da hora de trabalho (em reais)
e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário.
Adicionando '10%' sobre o valor calculado.
"""

hora_trabalho_valor = float(input('Informe o valor da hora de trabalho em reais: '))
hora_trabalho_quant = float(input('Informe a quantidade da horas trabalhadas: '))


sal = hora_trabalho_quant * hora_trabalho_valor
acres = 10.0 / 100.0
sal_com_acres = sal + (sal * acres)


print('O salário com dez por cento de acréscimo será:', sal_com_acres)
