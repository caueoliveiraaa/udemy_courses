"""
19) Leia um valor de um volume em litros e apresente-o
convertido em metros cúbicos m³. A fórmula de conversão é: M = L/1000,
sendo o L o volume em litros e M o volume em metros cúbicos.
"""

lt = float(input('Digite o volume em litros: '))
convertido_mc = lt / 1000

print(f'O volume em litros convertido para metros cúbicos é: {convertido_mc}')
