#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

#Declarar.
n1: int = 0
n2: int = 0
maior: int = 0
menor: int = 0
dif: int = 0

#Início.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

dif = maior - menor

print(f"A diferença do maior pelo menor valor é {dif}.")

#Fim.
