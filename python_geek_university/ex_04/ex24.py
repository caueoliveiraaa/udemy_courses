"""
24) Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.
"""


metros_quad = float(input('Digite o valor de área em metros quadrados: '))
convertido_acres = metros_quad * 0.000247


print(f'O valor de área convertido para acres é: {convertido_acres}')
