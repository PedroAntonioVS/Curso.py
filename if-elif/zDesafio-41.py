# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
while True:
    from datetime import date
    birth = int(input('Enter your birth year: '))
    year_old = date.today().year - birth
    if year_old >= 1 and year_old <10:
        print(f'He is a {year_old} years old')
        print('Mirin')
    elif year_old >= 9 and year_old < 15:
        print(f'He is a {year_old} years old')
        print('Infantil')
    elif year_old >= 14 and year_old <20:
        print(f'He is a {year_old} years old')
        print('Junior')
    elif year_old >= 19 and year_old < 25:
        print(f'He is a {year_old} years old')
        print('Senior')
    elif year_old >= 25:
        print(f'He is a {year_old} years old')
        print('Master')
    else:
        print(f'He is {year_old} years old')
        print('its still very young')
