#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 

#Declarar
ql: int = 0
tempoPercurso: int = 0
v: int = 0

#Início
tempoPercurso = int(input("Digite o tempo do percurso: "))
v = int(input("Digite a velocidade média: "))
ql = tempoPercurso * v / 12
print(f"Para poder percorrer esse percurso, será gasto {ql} litros de gasolina.")

#Fim
