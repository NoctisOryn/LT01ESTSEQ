#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
import math

#Declarar
a: int = 0
b: int = 0
c: int = 0

def calc_raíz():
   global a
   global b
   global c

   delta = b**2 - 4 * a * c
   
   if delta > 0: 
      r1 = (-b + math.sqrt(delta)) / (2*a)
      r2 = (-b - math.sqrt(delta)) / (2*a)
      print(f"As raízes são {r1} e {r2}.")

   elif delta < 0:
      print("Os coeficientes recebidos não possuem raíz real.")

   else: 
      r = -b / (2*a)
      print(f"A raíz é {r}.")

def main():
   global a
   global b
   global c
   a = int(input("Digite um número inteiro: "))
   b = int(input("Digite outro número inteiro: "))
   c = int(input("Digite mais um número inteiro: "))
   calc_raíz()

if (__name__ == '__main__'):
   main()
