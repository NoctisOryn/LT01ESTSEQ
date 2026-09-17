#Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

#Declarar
a1: int = 0
a2: int = 0
a3: int = 0

#Início
a1 = int(input("Digite o primeiro ângulo: "))
a2 = int(input("Digite o segundo ângulo: "))
a3 = 180 - (a1 + a2)
print(f"O seu terceiro ângulo possui {a3} graus.")

#Fim
