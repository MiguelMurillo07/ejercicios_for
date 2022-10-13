# Hacer el diagrama de Flujo y programa en Python que simule n lanzamientos de un dado.


print("--------------------------------------")
print("---------Lanzamiento de Dado----------")
print("--------------------------------------")

# input

import random

n = int(input("Digite el número de veces que quiere que sea lanzado el dado: "))

contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

k = n

for i in range(n):
    i = random.randint(1, 6)
    if i == 1:
        contador1 = contador1 + 1

    elif i == 2:
        contador2 += 1

    elif i == 3:
        contador3 += 1

    elif i == 4:
        contador4 += 1

    elif i == 5:
        contador5 += 1

    elif i == 6:
        contador6 += 1


print("\nEl dado cayó "+str(k)+ " veces.")
print("\n A continuación se marcarán los lados del que cayó el dado:")
print("1. ")
        
