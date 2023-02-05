"""
12) Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros
e M em milhas.
"""

ml = float(input('Digite a velocidade em milhas: '))
km = ml *  1.609344
print(f"Milhas: {ml}\nKM: {km}")
