#Faça um programa que leie um número da 0 a 9999 e mostre na tela cada um dos digitos separados EX:
#Digite um numero:1834
#Unidade 4 Dezena 3 centena 8 milhar 1
numero = int(input("Digite um numero: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("Analizando o numero {}".format(numero))
#if e elif foi um texte
if milhar>=1:
    print("Unidade: {}".format(unidade))
    print("Dezena: {}".format(dezena))
    print("Centena: {}".format(centena))
    print("Milhar: {}".format(milhar))
elif milhar == 0 and centena >=1:
    print("Unidade: {}".format(unidade))
    print("Dezena: {}".format(dezena))
    print("Centena: {}".format(centena))
elif centena == 0 and dezena >=1:
    print("Unidade: {}".format(unidade))
    print("Dezena: {}".format(dezena))
else:
    print("Unidade: {}".format(unidade))