#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

#Declarar.
n1: int = 0
n2: int = 0

def calc_cres():
   global n1
   global n2 

   if n1 > n2:
     print(f"{n2}, {n1}")
   else:
     print(f"{n1}, {n2}")

def main():
   global n1
   global n2

   n1 = int(input("Digite um número inteiro: "))
   n2 = int(input("Digite outro número inteiro: "))
   while n1 == n2:
     n2 = int(input("Digite um número diferente do primeiro: "))
   calc_cres()

if (__name__ == '__main__'):
   main()
