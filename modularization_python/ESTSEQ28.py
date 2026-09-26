#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
#----------------------------------------------------
# |   Venda Mensal  |   Preço Atual  |  Preço Novo  |
#----------------------------------------------------
# |     < 500       |      < 30      |     +10%     |
# |  >=500 e <1000  |   >=30 e <80   |     +15%     |
# |     >= 1000     |      >=80      |     -05%     |
#Obs.: para outras condições, preço novo será igual ao preço atual.

#Declarar.
p: float = 0.0
vm: float = 0.0

def calc_preco(p, v):
   res: float = 0.0
   if p < 30 and v < 500:
      res = p * 1.1
   elif p >= 30 and p < 80 and v >= 500 and v < 1000:
      res = p * 1.15
   elif p >= 80 and v >= 1000:
      res = p * 0.95
   else:
      res = p
   return res
def main():
   global p
   global vm
   p = float(input("Digite o valor do produto: "))
   vm = float(input("Digite o valor da venda mensal: "))
   print(f"O novo valor será de R${calc_preco(p, vm)}.")

if (__name__ == '__main__'):
   main();
