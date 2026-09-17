#Calcule e mostre o quadrado dos números entre 10 e 150.

#Declarar.
quad: int = 0
i: int = 0

#Início.
for i in range(10, 151):
   quad = i ** 2
   print(f" A raíz quadrada de {i} é {quad}")
#Fim.
