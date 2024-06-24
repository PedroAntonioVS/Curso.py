#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
number_1 = int(input('Enter one integer number: '))
number_2 = int(input('Enter another integer number:'))
if number_1 > number_2:
    print(f'The number {number_1} is greater then number {number_2}')
elif number_2 > number_1:
    print(f'The number {number_2} is greater then number {number_1}')
else:
    print('The numbers are equal')