#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
#----------------------------------------------------
# |   Venda Mensal  |	Preço Atual  |	Preço Novo  |
#----------------------------------------------------
# |     < 500       |  	   < 30      | 	 +10%     |
# |  >=500 e <1000  |   >=30 e <80   |     +15%     |
# |     >= 1000     |      >=80      |     -05%     |
#Obs.: para outras condições, preço novo será igual ao preço atual.

#Declarar.
p: float = 0.0
m: float = 0.0
pn: float = 0.0

#Início.
p = float(input("Digite o preço atual: "))
m = float(input("Digite a venda mensal: "))

if m < 500 and p < 30:
   pn = p * 1.1
   print(f"O preço novo será R${pn}.")
elif m >= 500 and m < 1000 and p >= 30 and p < 80:
   pn = p * 1.15
   print(f"O preço novo será R${pn}.")
elif m >= 1000 and p >= 80:
   pn = p * 0.95
   print(f"O preço novo será R${pn}.")
else:
   pn = p
   print(f"O preço permanecerá o mesmo: R${pn}")
#Fim.
