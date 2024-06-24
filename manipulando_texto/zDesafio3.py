#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo
while True:
    print("Programa para analizar se sua cidade natal tem santo no nome")
    cidade = str(input("Digite o nome da sua cidade natal: ")).strip()
    print(cidade)
    if ("santo","são","sao" in cidade.lower()):
        print("Sua Cidade é santa")
    else:
        print("Sua Cidade não tem nome santo")