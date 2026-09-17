#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

#Declarar.
n1: float = 0.0
maior: float = 0.0
menor: float = 0.0
i: int = 0

#Início.
for i in range(1, 101):
   n1 = float(input("Digite um número: "))
   while n1 < 0:
      n1 = float(input("Digite um número maior que zero: "))
   if i == 1:
      maior = n1
      menor = n1
   if n1 >= maior:
      maior = n1
   if n1 <=  menor:
      menor = n1
print(f"O maior número foi {maior}, enquanto o menor foi {menor}.")
#Fim.
