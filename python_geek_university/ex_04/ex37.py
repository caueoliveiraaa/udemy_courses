"""
37) Faça um programa que leia o valor de um produto e imprima
o valor com desconto, tendo em vista que o desconto foi de 12%.
"""


# valor_original = float(input('Informe o valor do produto: '))
# valor_desconto = 12.0 / 100.0
# valor_final = valor_original - (valor_desconto * valor_original)

# print('O produto com o desconto de doze por cento custará', valor_final)

# Or

produto_bruto = float(input("Digite o valor do produto: "))

produto_desconto = produto_bruto - (produto_bruto*0.12)

print("\nO valor do produto com desconto:\n%.2f" % produto_desconto)