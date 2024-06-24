#for c in range (1,10):
#    passo
#pega 

#for c in range (0,3):
#    passo
#    pula
#passo 
#pega

#for c in range (0,3):
    #if moeda:
#        pega
#    passo 
#    pula
#passo
#pega

for c in range (1,6):
    print('hello')
print('End') # print 5x hello 

for c in range (1,6):
    print(c)
print('End') # print contegem de 1 a 5 

for c in range (6, 1, -1):
    print(c)
print('End') # contagem regrassiva

for c in range(0, 7, 2):
    print(c)
print('End') # contagem pulando 2

i= int(input('inicio: '))
f= int(input('fim: '))
p= int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('End')

s = 0
for c in range (0,4):
    n = int(input('Digite um valor: '))
    s = s + n 
print(f'A soma dos valores é de: {s}')
