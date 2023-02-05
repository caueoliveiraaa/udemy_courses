"""
23) Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Por exemplo: 1988, 1992, 1996.
"""

check_year = True
while check_year:
    try:
        year = int(input('informe o ano: '))
        if ((year % 400) == 0) or (((year % 4) == 0) and (year % 100) != 0):
            print(f'ano {year} é bissexto!')
            check_year = False
        else:
            print(f'ano {year} não é bissexto!')
            check_year = False
    except Exception as e:
        print(f'ocorreu um erro:\n{e}\ntente informar um ano válido.')
        