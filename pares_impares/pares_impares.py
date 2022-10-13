# Hacer el diagrama de Flujo y programa en Python, que lea 100 números enteros y que averigue e imprima cuantos son pares e impares


print("----------------------------------------")
print("--------Números Pares e Impares---------")
print("----------------------------------------")


# input


cant_pares = 0
cant_impares = 0

# processing

for i in range(1, 100):
    if (i%2) == 0:
        cant_pares = cant_pares + 1
    else:
        cant_impares = cant_impares + 1

print("\nLa cantidad de números pares son "+str(cant_pares)+ " e impares son "+str(cant_impares))