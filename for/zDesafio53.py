#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto [letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print("Temos um palindromo!")
else:
    print('A frase nao é um palindromo')