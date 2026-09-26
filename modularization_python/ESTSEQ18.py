#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

#Declarar.
n1: int = 0
n2: int = 0

#Início.
def calc_dif():
   global n1
   global n2

   if n1 >= n2:
      dif = n1 - n2
      print(f"{n1} - {n2} = {dif}")
   else:
      dif = n2 - n1
      print(f"{n2} - {n1} = {dif}")

def main():
   global n1
   global n2
   n1 = int(input("Digite um número: "))
   n2 = int(input("Digite outro número inteiro: "))
   calc_dif()

if (__name__ == '__main__'):
   main()
#Fim.

