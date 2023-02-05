"""
43) Escreva um programa de ajuda para vendedores. A partir de um valor
total lido, mostre:
 - O total a pagar com desconto de 10%
 - O valor de cada parcela, no parcelamento de 3x sem juros;
 - A comissão do vendedor, no caso da venda ser a vista('5%' sobre o valor com desconto)
 - A comissão do vendedor, no caso da venda ser parcelada('5%' sobre o valor total)
"""

valor = float(input('infomre o valor da compra: '))
forma_pag = int(input('Digite 1 para pagar a vista, ou 2 para pagar parcelado: '))
desconto10 = 0.1 
valor_desconto = valor - (valor * desconto10)
print("Desconto 10% ", valor_desconto)
valor_parcela = valor_desconto / 3
print("Valor de 3x: ", valor_parcela)
comissao = valor_desconto * (5.0 / 100.0 )
print('Comissão do vendedor: ', comissao)
comissao = valor * (5.0 / 100.0 )
print('Comissão do vendedor: ', comissao)