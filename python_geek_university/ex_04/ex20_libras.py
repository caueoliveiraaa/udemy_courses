"""
20) Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, snedo K a massa em quilogramas
e L a massa em libras.
"""

quilo_gms = float(input('Digite o valor de massa em quilogramas: '))
convertido_lb = quilo_gms / 0.45
print(f'O valor de massa convertido para libras é: {convertido_lb}')
