"""
40) Uma empresa contrata um encanador a R$30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantida liquida que deverá ser paga. Sabendo-se que são descontandos '8%' para imposto de renda.
"""

dias_trabalhados_quant = int(input('Infome a quantidade de dias trabalhados neste mês: '))
valor_dias_trabalhados = dias_trabalhados_quant * 30.0
imposto = 8.0 / 100.0
sal_liq = valor_dias_trabalhados - (imposto * valor_dias_trabalhados)
print('O salário líquido é:', sal_liq)
