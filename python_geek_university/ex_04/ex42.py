"""
42) Receba o salário-base de um funcionário. Calcule e imprima o salário
a receber, sabendo-se que esse funcionário tem gratificação de '5%' sobre o salário-base.
Além disso, ele paga '7%' de imposto sobre o salário-base.
"""

sal_base = float(input('Informe o slário base do funcionário: '))
gratificacao = 5.0 / 100.0
imposto = 7.0 / 100.0
sal_com_grat = sal_base + (sal_base * gratificacao)
sal_desc_imposto = sal_com_grat - (sal_com_grat * imposto)

print('O salário baso do funcionário com 5 por cento de acréscimo e 7 por cento de imposto será:', sal_desc_imposto)
