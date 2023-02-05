"""
16) Usando switch, escreva um programa que leia um inteiro entre 1 e 12
e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2,
e assim por diante.
"""

meses = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}
opcao = int(input("Informe o dia da semana usando números de 1 a 7: "))
print(f"Dia selecionado: {meses[opcao]}")