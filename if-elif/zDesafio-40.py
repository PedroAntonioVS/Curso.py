#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
grade_1 = float(input('Enter your first grade: '))
grade_2 = float(input('Enter your second grade: '))
average = (grade_1 + grade_2) / 2
if average == 6:
    print(f'Your average is {average}')
    print('You reached the average, its approved ')
elif average >= 5 and average < 6:
    print(f'Your average is {average}')
    print('Your are in recovery ')
elif average > 6:
    print(f'Your average is {average}')
    print('You are above average, approved')
else:
    print(f'Your average is {average}')
    print('You are disapproved')
