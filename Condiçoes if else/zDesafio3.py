#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um numero inteiro: '))
if numero % 2 == 0:
    print('O numero é par.')
else:
    print('O numero é impar.')