#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

#Declarar.
i: float = 0.0
tipo: int = 0
m: float = 0.0

#Início.
i = float(input("Quanto você deseja depositar? "|))
while tipo != 1 and tipo != 2:
   tipo = int(input("Digite o tipo de investimento: [1]Poupança   [2]Renda Fixa"))
if tipo == 1:
   m = i * 1.03
   print(f"O montante será de R${m}.")
else
   m = i * 1.05
   print(f"O montante será de R${m}.")
#Fim.
