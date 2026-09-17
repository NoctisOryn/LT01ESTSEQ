#Receba um número. Calcule e mostre os resultados da tabuada desse número.

#Declarar.
n1: int = 0
i: int = 0
tab: int = 0

#Início.
n1 = int(input("Digite um número: "))
for i in range (1, 11):
   tab = n1 * i
   print(f"{n1} × {i} = {tab}")
#Fim.
