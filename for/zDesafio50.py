#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
print('Digite 6 numeros inteiros')
for i in range (1,7): 
    num = int(input('numero: '))
    if num % 2 == 0:
       soma += num
       cont += 1
if cont == 1:
    print(f'voce informou {cont} numero par e a soma dele foi de: {soma}')
else:
    print(f'voce informou {cont} numeros pares e a soma deles foi de: {soma}')