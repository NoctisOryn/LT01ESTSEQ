#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

#Declarar
n1: int = 0

def calc_div():
   global n1
   if n1 % 2 == 0 and n1 % 3 == 0:
      print(f"{n1} é divisível por 2 e 3.")
   elif n1 % 2 == 0:
      print(f"{n1} é divisível por 2.")
   elif n1 % 3 == 0:
      print(f"{n1} é divisível por 3.")
   else:
      print(f"{n1} não é divisível por 2 e 3.")

def main():
   global n1

   n1 = int(input("Digite um número: "))
   calc_div()

if (__name__ == '__main__'):
   main()
