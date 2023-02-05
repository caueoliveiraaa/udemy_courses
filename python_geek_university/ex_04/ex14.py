"""
14) Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * r / 180, sendo G o ângulo em graus
e R em radianos e r = 3.14.
"""

angulo_graus = float(input('Digite o ângulo em graus: '))
radianos = angulo_graus * 3.14 / 180


print(f'Radianos: {radianos}')
