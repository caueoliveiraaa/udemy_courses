"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre
o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadaa anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliaçõ Semestral: 3; Exame final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

tra_lab = float(input('Informe a nota do trabalho do laboratorio: '))
ava_sem = float(input('Informe a nota da avaliacao semestral: '))
exa_fin = float(input('Informe a nota do exame final: '))
p1 = 2
p2 = 3
p3 = 5

med_pon = ((tra_lab * p1) + (ava_sem * p2) + (exa_fin * p3)) / (p1 + p2 + p3)
if med_pon >= 0 and med_pon <= 2.9:
    print(f'Aluno reprovado!\nMedia ponderada: {med_pon}')
elif med_pon > 2.9  and med_pon <= 4.9:
    print(f'Aluno de recuperacao!\nMedia ponderada: {med_pon}')
else:
    print(f'Aluno aprovado!\nMedia ponderada: {med_pon}')

