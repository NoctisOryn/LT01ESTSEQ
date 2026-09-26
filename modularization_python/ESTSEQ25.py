#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro. 

#Declarar.
hi: int = 0
hf: int = 0
mi: int = 0
mf: int = 0

def calc_jogo():
   global hi
   global hf
   global mi 
   global mf

   if hi < hf and mi <= mf:
      h = hf - hi
      m = mf - mi
      print(f"O jogo durará {h}h{m}.")
   elif hi < hf and mi > mf:
      h = hf - hi - 1
      m = (mf + 60) - mi
      print(f"O jogo durará {h}h{m}.")
   elif hi > hf and mi <= mf:
      h = (24 - hi) + hf
      m = mf - mi
      print(f"O jogo durará {h}h{m}.")
   elif hi == hf:
      m = mf - mi
      print(f"O jogo durará {m} min.")
   else:
      h = (24 - hi) + hf - 1
      m = (mf + 60) - mi
      print(f"O jogo durará {h}h{m}.")

def main():
   global mi
   global mf
   global hi
   global hf

   hi = int(input("Que horas iniciará o jogo? "))
   hf = int(input("Que horas finalizará o jogo? "))
   mi = int(input("Em que minutos iniciará o jogo? "))
   mf = int(input("Em que minutos finalizará o jogo? "))
   calc_jogo()

if (__name__ == '__main__'):
   main()
