#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
def cal_imc(height, weight):
    imc = height / (weight ** 2)
    return imc
def classifica(imc):
    if imc < 18.5:
        return 'Under weight'
    elif 18.5 <= imc < 25:
        return 'Ideal weight'
    elif 25 <= imc < 30:
        return 'Overweight'
    elif 30 <= imc < 40:
        return 'Obesity'
    elif imc >= 40:
        return 'Morbid obesity'
height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))
imc = cal_imc(height, weight)
print(f'Your IMC is :{imc:.2f} {classifica(imc)}')