#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

#Declarar.
n: int = 0
ec: float = 0.0
t: int = 0
vm: int = 0

#Início.
n = int(input("Digite o número de voltas: "))
ec = float(input("Digite a extensão do circuito em metros: "))
t = int(input("Digite o tempo em minutos: "))

vm = (ec * n) / (t * 60) * 3.6
print(f"A velocidade média é {vm}km/h") 
#Fim.
