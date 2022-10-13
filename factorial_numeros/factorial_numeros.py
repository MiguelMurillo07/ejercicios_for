# Dado un número n calcular el factorial. Hacer diagrama de flujo y programa en Python que calcule el factorial del número y lo imprima junto con el número leído.


print("-----------------------------------")
print("------------Factorial--------------")
print("-----------------------------------")


# input

n = int(input("\nDigite el número que quiera calcular su factorial: "))
fact = 1

# processing


for i in range(1, n+1):
    fact = fact * i

# output

print("El número "+str(n)+ " tiene como factorial "+str(fact))