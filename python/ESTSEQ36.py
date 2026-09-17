#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

#Declarar.
n1: int = 0
box1: float = 1.0
box2: int = 1
i: int = 0

#Início.
n1 = int(input("Digite um número: " ))

for i in range(1, n1 + 1, 1):
   box2 = box2 * i
   box1 = box1 + (1/box2)

print(f"A série de {n1} é {box1}")
#Fim.
