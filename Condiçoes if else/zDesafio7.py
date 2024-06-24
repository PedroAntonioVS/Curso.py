#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado2 + lado1 > lado3 and lado3 + lado1 > lado2:
    print('Sim pode ser um triangulo')
else:
    print('Não pode formar um triangulo')
