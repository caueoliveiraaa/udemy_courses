"""
17) Leia um valor de comprimento em centímetros e apresente-o convertida
em centímetros. A fórmula de conversão é: P = C/2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

cm = float(input('Digite o valor em centímetros: '))
convertido_polegadas = cm / 2.54
print(f'O valor em centímetros convertido para polegadas é: {convertido_polegadas}')
