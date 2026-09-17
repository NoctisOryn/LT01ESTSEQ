#Receba um número inteiro. Calcule e mostre o seu fatorial.

#Declarar.
n1: int = 0
i: int = 0
box: int = 1

#Início.
n1 = int(input("Digite um número inteiro: "))

for i in range (n1, 0, -1):
   box = box  * i

print(box)
#Fim.
