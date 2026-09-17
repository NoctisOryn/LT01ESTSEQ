#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

#Declarar.
n1: int = 0
i: int = 0
box: float = 0.0

#Início.
n1 = int(input("Digite um número: "))

for i in range(1, n1 + 1):
   box = box + (1/i)
print(box)

#Fim.
