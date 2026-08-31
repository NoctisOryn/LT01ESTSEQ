#Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

#Declarar
import math
c1: int = 0
c2: int = 0
h: float = 0.0

#Início
c1 = int(input("Digite o primeiro cateto: "))
c2 = int(input("Digite o segundo cateto: "))
h = math.sqrt(c1 **2 + c2 ** 2)
print(f"A hipotenusa é igual a {h}.")

#Fim
