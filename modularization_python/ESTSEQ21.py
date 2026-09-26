#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#|---------------------------------------------|
#|   Se a média for >= 6,0 exibir “APROVADO”;  |
#|---------------------------------------------|
#|Se a média for >= 3,0 E < 6,0 exibir “EXAME”;|
#|---------------------------------------------|
#|    Se a média for < 3,0 exibir “RETIDO”.    |
#|---------------------------------------------|

#Declarar.
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0

def calc_nota():
   global n1
   global n2
   global n3
   global n4

   m = (n1 + n2 + n3 + n4) / 4
   if m >= 6.0:
      print("APROVADO")
   elif m >= 3.0 and m < 6.0:
      print("EXAME")
   else:
      print("RETIDO")

def main():
   global n1
   global n2
   global n3
   global n4

   n1 = float(input("Digite a primeira nota: "))
   n2 = float(input("Digite a segunda nota: "))
   n3 = float(input("Digite a terceira nota: "))
   n4 = float(input("Digite a quarta nota: "))
   calc_nota()

if (__name__ == '__main__'):
   main()
