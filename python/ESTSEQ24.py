#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

#Declarar.
n1: int = 0

#Início.
n1 = int(input("Digite um número inteiro: "))
if n1 % 2 == 0 and n1 % 3:
   print(f"O número {n1} é divisível por 2 e 3.")
elif n1 % 2 == 0:
   print(f"O número {n1} é divisível por 2.")
elif n1 % 3 == 0:
   print(f"O número {n1} é divisível por 3.")
else:
   print(f"O número {n1} não é divsível por 2 e 3.")
#Fim.
