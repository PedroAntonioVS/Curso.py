#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
car = int(100000)
print('Modos de pagamentos')
print('[ 1 ] A vista dinheiro / cheque: 10% de desconto')
print('[ 2 ] A vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2X no cartão: preço normal')
print('[ 4 ] 3X ou mais no cartão: 20% de juros')
pagamento = input('Escolha seu modo de pagamento: ').strip()
if pagamento == '1':
    total = car - (car * 10 / 100)
    print(f'O valor do carro ficou R$ {total:.2f}')
elif pagamento == '2':
    total = car - (car * 5 / 100)
    print(f'O valor do carro ficou R$ {total:.2f}')
elif pagamento == '3':
    print(f'O valor final da compra ficou R$ {car}')
elif pagamento == '4':
    parcelas = int(input('Quantas parcelas? '))
    total = car + (car * 20 / 100)
    total_parcelas = total / parcelas
    print(f'O seu carro foi parcelado em {parcelas}X parcelas de R$ {total_parcelas:.2f} o valor total será {total:.2f}')
else:
    print('Opção invalida tente novamente!')