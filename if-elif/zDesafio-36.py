#Testando codar em ingles :)
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
house = float(input('What is the value of the house? '))
salary = float(input('What is your salary? '))
years = int(input('How many years do you want to pay? '))
loan = house / (years * 12)
accept = salary * 30 / 100
if loan <= accept:
    print('Loan accepted')
else:
    print('Loan denied')