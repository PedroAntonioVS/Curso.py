#Crie um programa q leia o nome de uma pessoa completo e mostre O nome com todas as letras maiusculas, O nome com todas minusculas, Quantas letras letras ao todo sem considerar espaços, Quantas letras tem o primeiro nome
while True:
    nome = str(input("Digite seu nome: ")).strip()
    print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
    print("Seu nome com as letras maiúsculas é: {}".format(nome.upper()))
    print("Seu nome com as letras minúsculas é: {}".format(nome.lower()))
    separa = nome.split()
    print("Seu primeiro nome tem {} letras".format(len(separa[0]))) 