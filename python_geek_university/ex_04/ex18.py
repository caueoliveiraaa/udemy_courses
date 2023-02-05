"""
18) Leia um valor de um volume em metros cúbicos m³ e apresente-o
convertido em litros. A fórmula de conversão é: L = 1000 * M,
sendo L o volume em litros e M o volume em metros cúbicos
"""

metros_c = float(input('Digite o volume em metros cúbicos: '))
convertido_lt = 1000 * metros_c

print(f'O valor em metros cúbicos convertido para litros é: {convertido_lt}')
