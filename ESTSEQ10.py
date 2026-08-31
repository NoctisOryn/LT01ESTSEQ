#Receba 2 números reais. Calcule e mostre a diferença desses valores.

#Declarar
import math
n1: float = 0.0
n2: float = 0.0
dif: float = 0.0

#Início
n1 = float(input("Digite qualquer número real: "))
n2 = float(input("Digite outro número real: "))
dif = abs(n1 - n2)
print(f"A diferença entre os números é {dif}.")
#FIm