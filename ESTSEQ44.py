#Receba o número da base e do expoente. Calcule e mostre o valor da potência.

#Declarar.
base: int = 0
expoente: int = 0
resultado: int = 1
i: int = 0

#Início.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

for i in range(1, expoente + 1):
    resultado = resultado * base

print(f"O resultado da potência é {resultado}.")

#Fim.
