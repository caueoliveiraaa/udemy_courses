"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 6 pontos.
"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
p1 = 1
p2 = 2

med_pon = ((n1 * p1) + (n2 * p1) + (n3 * p2)) / (p1 + p1 + p2)
if med_pon >= 6:
    print(f'Aluno aprovado!\nMedia ponderada: {med_pon}')
else:
    print(f'Aluno reprovado!\nMedia ponderada: {med_pon}')