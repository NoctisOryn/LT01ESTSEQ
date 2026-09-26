#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#Declarar.
n1: int = 0
ant: int = 1
atual: int = 0
temp: int = 0
i: int = 0

#Início.
n1 = int(input("Digite um número inteiro: "))
for i in range(1,n1 + 1):
   temp = atual 
   atual = ant + atual
   ant = temp
   print(atual)
#Fim.
