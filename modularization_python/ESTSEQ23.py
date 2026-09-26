#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

#Declarar.
n1: int = 0
n2: int = 0
n3: int = 0
n4: int = 0

def calc_cresc():
   global n1
   global n2
   global n3
   global n4

   if n4 <= n1:
     print(f"{n4}, {n1}, {n2}, {n3}.")
   elif n4 > n1 and n4 <= n2:
     print(f"{n1}, {n4}, {n2}, {n3}.")
   elif n4 > n2 and n4 <= n3:
     print(f"{n1}, {n2}, {n4}, {n3}.")
   else:
     print(f"{n1}, {n2}, {n3}, {n4}.")

def main():
   global n1
   global n2
   global n3
   global n4

   n1 = int(input("Digite o primeiro número: "))
   n2 = int(input("Digite o segundo número: "))
   while n2 < n1 :
      n2 = int(input("Digite um número maior que o primeiro: "))
   n3 = int(input("Digite o terceiro número: "))
   while n3 < n2:
      n3 = int(input("Digite um número maior que o segundo: "))
   n4 = int(input("Digite o quarto número: "))
   calc_cresc()

if (__name__ == '__main__'):
   main()
