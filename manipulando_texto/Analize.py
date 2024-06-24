frase="Curso em Video Python"
#Conta o tamnho da frase
print(len(frase))
#Conta quantos o tem dentro da frase
print(frase.count("o"))
#Conta quantos o tem dentro da frase apartir da casa 0 a 13
print(frase.count("o",0,13))
#Conta quantos o tem dentro da frase apartir da casa 0 a 14 
print(frase.count("o",0,14))
#Procura as letras deo e mostra sua casa inicial 
print(frase.find("deo"))
#Procura a palavra Androide e mostra sua casa inicial como nao existe apresenta como -1
print(frase.find("Androide"))
#Verificando se a palavra curso esta dentro da frase
print("Curso"in(frase))
#troca a palavra python por androide 
print(frase.replace("python","Androide"))
#trasformando todas as letras maiusculas
print(frase.upper())
#Trasformando todas as letras minusculas
print(frase.lower())
#Apenas a primeira letra de frase maiuscula
print(frase.capitalize())
#Todo inicio de palavra vai ter sua primeira letra maiuscula
print(frase.title())
