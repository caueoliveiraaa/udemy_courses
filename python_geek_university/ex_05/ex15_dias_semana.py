"""
15) Usando swicth, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2,
e assim por diante.
"""

dias_sema = {2:"Segunda-feira", 3:"Terça-feira", 4:"Quarta-feira", 5:"Quinta-feira", 6:"Sexta-feira", 7:"Sábado", 1:"Domingo"}
opcao = int(input("Informe o dia da semana usando números de 1 a 7: "))
print(f"Dia selecionado: {dias_sema[opcao]}")