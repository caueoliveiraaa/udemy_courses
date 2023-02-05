"""
36) Leia a altura e o raio de um cilindro círcular e imprima
o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * raio² * altura, onde r = 3.141592
"""

alt = float(input('Informe a altura do cilindro: ')) 
r =  float(input('Informe o raio do mesmo: '))
v = 3.141529 * (r * r) * alt
print(f'O volume do cilindro é: {v}')
