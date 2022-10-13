# Hacer el diagrama de Flujo y programa en Python, que averigue e imprima cuantos múltiplos de 7, cuantos múltiplos de 9 hay en los números comprendidos entre 1000 y 5000.


print("-----------------------------------")
print("--------Multiplos de 7 y 9---------")
print("-----------------------------------")


# input

m7 = 0
m9 = 0

# processing

for i in range(1000, 5001):
    if i%7 == 0:
        m7 += 1

    if i%9 == 0:
        m9 += 1


print("\nLos múltiplos de 7 en toda la cadena son "+str(m7))
print("\nLos múltiplos de 9 en toda la cadena son "+str(m9))
