"""
52) Três amigos jogaram na loteria. Caso eles ganhem,
o prêmio deve ser repartido porporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

valor_prem = float(input('Informe o valor do prêmio: '))
apost_a = float(input('Informe o valor investido pelo apostador A: '))
apost_b = float(input('Informe o valor investido pelo apostador B: '))
apost_c = float(input('Informe o valor investido pelo apostador C: '))


total_apost = apost_a + apost_b + apost_c
porcen_a = (apost_a / total_apost) * valor_prem
porcen_b = (apost_b / total_apost) * valor_prem
porcen_c = (apost_c / total_apost) * valor_prem


if (apost_a > apost_b and apost_a > apost_c):
    print(f'O apostador A apostou mais que os outros e receberá: {porcen_a}')
    print(f'O apostador B receberá: {porcen_b}')
    print(f'O apostador C receberá: {porcen_c}')

elif(apost_b > apost_a and apost_b > apost_c):
    print(f'O apostador B apostou mais que os outros e receberá: {porcen_b}')
    print(f'O apostador A receberá: {porcen_a}')
    print(f'O apostador C receberá: {porcen_c}')
    
else:
    print(f'O apostador C apostou mais que os outros e receberá: {porcen_c}')
    print(f'O apostador B receberá: {porcen_b}')
    print(f'O apostador A receberá: {porcen_a}')