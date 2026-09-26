#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

#Declarar.
tipo: int = 0
rend: float = 0.0

def calc_rend(t, r):
   if tipo == 1:
      res = r * 1.03
   else:
      res = r * 1.05
   return res

def main():
   global tipo
   global rend
   rend = float(input("Digite quanto deseja depositar: "))
   while tipo != 1 and tipo != 2:
      tipo = int(input("Digite o tipo de investimento: [1] Poupança; [2] Renda fixa. "))
   print(f"O rendimento foi R${calc_rend(tipo, rend)}.")

if (__name__ == '__main__'):
   main();
