#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salario: '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
elif salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
print(f'Seu salario de {salario:.2f} reais foi para {aumento:.2f} reais')