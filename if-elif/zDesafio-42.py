#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado2 + lado1 > lado3 and lado3 + lado1 > lado2:
    print('Sim pode ser um triangulo ', end='')
    if lado1 == lado2 == lado3:
        print('Equilatero')
    elif lado1 != lado2 != lado3 != lado1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Não pode formar um triangulo')
