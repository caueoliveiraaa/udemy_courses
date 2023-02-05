"""
15) Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/r, sendo G o ângulo
em graus e R em radianos e r = 3.14.
"""

angulo_radianos = float(input('Digite o ângulo em radianos: '))
convertido_graus = angulo_radianos * 180 / 314
print(f'O ângulo em radianos convertido em graus será: {convertido_graus}')
