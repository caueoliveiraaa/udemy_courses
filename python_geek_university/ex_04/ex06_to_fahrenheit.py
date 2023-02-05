"""
6) Leia uma temperatura em gruas Celsius e apresente-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

temp_c = float(input('Digite a temperatura em grau celsius: '))
f = temp_c * (9.0 / 5.0) + 32.0
print(f'A temperatura convertida para Fahrenheit é {f}')