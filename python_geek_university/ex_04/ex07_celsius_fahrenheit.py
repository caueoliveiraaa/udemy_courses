"""
7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é: C = (F-32.0)*5.0/9.0,
sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

f = float(input('Digite a temperatura em Fahrenheit: '))
c = 5.0 * (f - 32.0) / 9.0
print(f'Fahrenheit: {f}\nCelsius: {c}')