# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero inteiro: '))
tot = 0
numeros = []
for i in range (1,num + 1):
    if num % i == 0:
        tot += 1
        numeros.append(i)
if tot >= 2:
    print(f'O numero {num} foi divisivel {tot} vezes.')
    print(f'Pelos numeros {numeros}')
else:
    print(f'O numero {num} foi divisivel {tot} vez.')
    print(f'Pelo numero {numeros}')
if tot == 2:
    print('Por isso é primo.')
else:
    print('E por isso ele não é primo.')