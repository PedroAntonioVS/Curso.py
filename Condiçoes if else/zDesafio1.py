#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('Vou pensar em um numero entre 0 e 5 tente adivinhar :)')
while True:
    cpu = randint (0,5)
    chute = int(input('Digite seu palpite: '))
    print('processando...')
    sleep(1)
    if chute == cpu:
        print(f'Parabens! voce acertou meu numero era o {cpu}')
        break
    else:
        print('Voce errou :( tente novamente: ')

