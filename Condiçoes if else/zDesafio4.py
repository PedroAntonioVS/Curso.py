#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = int(input('Digite a distancia da viagem em KM: '))
if distancia <= 200:
    preco = distancia * 0.5
    print(f'Sua viagem custara {preco::.2f} reais')
elif distancia > 200:
    preco = distancia * 0.45
    print(f'Sua viagem custara {preco:.2f} reais')