#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
sex = input('Enter your sex [ Man / Woman ]: ').strip().lower()
if sex == 'man':
    birth = int(input('Enter your birth age: '))
    year = date.today().year
    year_old = year - birth

    if year_old == 18:
        print(f'you are {year_old} years old its time to enlist.')

    elif year_old > 18:
        difference = year_old - 18
        print(f'You are {year_old} years old already passed {difference} years from enlisting.')
        difference_year = year - difference
        print(f'You should have enlisted in {difference_year}')

    elif year_old < 18:
        difference = 18 - year_old
        print(f'You have {year_old} years old yet {difference} years to enlist.')
        difference_year = year + difference
        print(f'You have to enlist in {difference_year}')
else:
    print('You are a woman you do not need to enlsit')
