"""
49) Faça um programa para ler o horário (hora, minuto e segundo)
de ínicio e duração em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""

ini_hor = input('hora: ')
ini_min = input('minutos: ') 
ini_seg = input('segundos: ')
print(ini_hor,'h',ini_min,'m',ini_seg,'s')
dur_seg = input('segundos: ')
print(dur_seg,'s')
fin_seg = int(ini_seg) + int(dur_seg)
ext_min = int(fin_seg / 60)
fin_seg = fin_seg % 60
fin_min = int(ini_min) + ext_min
ext_hor = int(fin_min / 60)
fin_min = fin_min % 60
fin_hor = int(ini_hor) + ext_hor
fin_dia = int(fin_hor/24)
fin_hor = fin_hor % 24
print(fin_dia,'d',fin_hor,'h',fin_min,'m',fin_seg,'s')