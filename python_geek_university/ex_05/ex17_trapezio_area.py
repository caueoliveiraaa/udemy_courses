"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
    A = ((basemaior + basemenor) * altura) / 2

    Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

base_maior = float(input('informe a maior base: '))
base_menor = float(input('informe a menor base: '))
altura = float(input('informe a altura: '))

area = (base_maior + base_menor) * altura / 2
print('area do trapezio: {area}')