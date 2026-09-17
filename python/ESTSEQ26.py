#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

#Declarar.
n1: int = 0
n2: int = 0

#Início.
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if  n1 >= n2:
   if n1 % n2 == 0:
      print(f"O número {n1} é múltiplo de {n2}.")
   else:
      print(f"O número {n1} não é múltiplo de {n2}.")
else:
   if n2 % n1 == 0:
      print(f"O número {n2} é múltiplo de {n1}.")
   else:
      print(f"O número {n2} não é múltiplo de {n1}.")
#Fim.
