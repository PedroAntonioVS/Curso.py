#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite o numero para ver sua tabuada: '))
for i in range(0,11):
    print(f'{num} X {i:2} = {num*i}')