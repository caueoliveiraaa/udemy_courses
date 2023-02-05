"""
44) Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário
deverá subir para atingir seu objetivo.
"""

alt_degrau = float(input('Informe a altura do degrau: '))
alt_total = int(input('Informe a altura de onde desejas chegar: '))
subida = alt_total / alt_degrau
print(f'Você terá que subir {subida} degraus.')
