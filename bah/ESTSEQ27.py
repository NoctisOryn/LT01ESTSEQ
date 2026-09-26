#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

#Declarar
nv: float = 0.0
ec: float = 0.0
temp: int = 0

def calc_vm(v, c, t):
   res: float = 0.0
   res = ((v * c) / (60 * t)) * 3.6
   return res

def main():
   global nv
   global ec
   global temp
   nv = float(input("Digite o número de voltas: "))
   ec = float(input("Digite a extensão do circuito em metros: "))
   temp = int(input("Digite o tempo em minutos: "))
   print(f"A velocidade média é {calc_vm(nv, ec, temp)}km/h.") 


if (__name__ == '__main__'): 
   main();
