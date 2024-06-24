#crie um programa que faça o computador jogar Jokenpô com você.
while True:
    from time import sleep
    from random import randint
    print('Lets play Jokenpô!')
    print('[ 1 ] for STONE')
    print('[ 2 ] for PAPER')
    print('[ 3 ] for SCISSORS')
    print('[ 4 ] for exit')
    itens = ('Stone', 'Paper', 'Scissors')
    computer = randint (0, 2)
    choice = input('Make your choice: ')
    if choice == '4':
        break
    elif choice == '1' or '2' or '3':
        print('Jo')
        sleep(0.5)
        print('ken')
        sleep(0.5)
        print('pô!')
        sleep(0.5)
        print('===============================')
        print(f'The computer chose {itens[computer]}')
        print(f'The player chose {itens[0]}')
        if computer == 0: # computer play stone
            if choice == '1':
                print('Draw')
            elif choice == '2':
                print('You Won')
            elif choice == '3':
                print('You lose')
            else:
                print('Error try again')
        if computer == 1: # computer play paper
            if choice == '1':
                print('You lose')
            elif choice == '2':
                print('Draw')
            elif choice == '3':
                print('You Won')
            else:
                print('Error try again')
        if computer == 2: # computer play Scissors
            if choice == '1':
                print('You Won')
            elif choice == '2':
                print('You lose')
            elif choice == '3':
                print('Draw')
    print('===============================')
