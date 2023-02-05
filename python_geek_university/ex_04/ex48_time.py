"""
48) Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
"""

seg = int(input('Infomre o valor em segundos: '))
h = seg // 3600
resto = seg % 3600
minu = resto // 60
seg = resto % 60
print(f'{h} hr {minu} min {seg} seg')