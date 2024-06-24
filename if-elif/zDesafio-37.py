#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. Aula Anterior
while True:
    import os
    nunber = int(input('Enter an integer number: '))
    print('Choose one of the conversion options.')
    print('1 - Convert to binary')
    print('2 - Convert to hexadecimal.')
    print('3 - Convert to octal.')
    print('4 - Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print(f'{nunber} converted to binary is {bin(nunber)}')
        print('=======================================')
        input('Press Enter to continue.')
        os.system('cls')
    elif choice == 2:
        print(f'{nunber} converted to hexadecimal is {hex(nunber)}')
        print('=======================================')
        input('Press Enter to continue.')
        os.system('cls')
    elif choice == 3:
        print(f'{nunber} converted to octal is {oct(nunber)}')
        print('=======================================')
        input('Press Enter to continue.')
        os.system('cls')
    elif choice == 4:
        break
    else:
        print('Invalid option, please try again.')  
