#Receba 2 valores reais. Calcule e mostre o maior deles.

#Declarar.
n1: float = 0.0
n2: float = 0.0

def calc_maior():
   global n1
   global n2

   if n1 > n2:
      print(f"{n1} é maior que {n2}.")
   elif n2 > n1:
     print(f"{n2} é maior que {n1}.")
   else:
      print(f"Ambos possuem o mesmo valor.")

def main():
   global n1
   global n2
   n1 = float(input("Digite um número real: "))
   n2 = float(input("Digite outro número real: "))
   calc_maior()

if (__name__ == '__main__'):
   main()
