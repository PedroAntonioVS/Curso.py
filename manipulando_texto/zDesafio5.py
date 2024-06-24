#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome=input("Digite seu nome completo: ").strip()
print("Seu primeiro nome é {}".format(nome.split()[0]))
print("Seu segundo nome é {}".format(nome.split()[-1]))
