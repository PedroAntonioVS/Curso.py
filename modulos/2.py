import math
catetooposto=float(input("Digite o cateto oposto: "))
catetoadijacente=float(input("Digite o cateto adjacente: "))
comprimento= math.sqrt(catetoadijacente**2 + catetooposto**2)
print("{:.2f}".format(comprimento))