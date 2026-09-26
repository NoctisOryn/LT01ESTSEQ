#Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

#Declarar.
n1: int = 0
n2: int = 0

def calc_mult():
   global n1
   global n2

   if n1 >= n2 and n1 % n2 == 0:
      print(f"{n1} é múltiplo de {n2}.")
   elif n2 > n1 and n2 % n1 == 0:
      print(f"{n2} é múltiplo de {n1}.")
   else:
      print(f"{n1} e {n2} não são múltiplos.")

def main():
   global n1
   global n2

   n1 = int(input("Digite um número: "))
   n2 = int(input("Digite outro número: "))
   calc_mult()

if (__name__ == '__main__'):
   main()
