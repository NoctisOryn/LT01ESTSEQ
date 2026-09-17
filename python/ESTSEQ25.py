#Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

#Declarar.
hi: int = 0
hf: int = 0
mi: int = 0
mf: int = 0
dH: int = 0
dM: int = 0

#Início.
hi = int(input("Digite a hora inicial do jogo: "))
mi = int(input("Digite os minutos inicial do jogo: "))
hf = int(input("Digite a hora final do jogo: "))
mf = int(input("Digite os minutos finais do jogo: "))

if hi < hf and mi <= mf:
   dH = hf - hi
   dM = mf - mi
   print(f"O jogo terá duração de {dH}h{dM}.")
elif hi < hf and mf < mi:
   dH = hf - hi - 1
   dM = (mf + 60) - mi
   print(f"O jogo terá duração de {dH}h{dM}.")
elif hf < hi and mi <= mf:
   dH = (24 - hi) + hf
   dM = mf - mi
   print(f"O jogo terá duração de {dH}h{dM}.")
else:
  dH = (24 - hi) + hf - 1
  dM = (mf + 60) - mi
  print(f"O jogo terá duração de {dH}h{dM}.")

#Fim.
