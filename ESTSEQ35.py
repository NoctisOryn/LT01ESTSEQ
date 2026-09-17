# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

#Declarar.
n1: int = 0
n2: int = 0
maior: int = 0
menor: int = 0
soma: int = 0
i: int = 0

#Início.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for i in range(menor, maior + 1):
    if i % 2 != 0:
        soma = soma + i

print(f"A soma dos números ímpares entre os valores é {soma}.")

#Fim.

