#Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).

#Declarar
import math
a: int = 0
b: int = 0
c: int = 0
delta: float = 0.0
r1: float = 0.0
r2: float = 0.0

#Início
a = int(input("Digite o coeficiente A da sua equação do 2° grau: (OBS: Não pode ser 0.) "))
b = int(input("Digite o coeficiente B da sua equação do 2° grau: "))
c = int(input("Digite o coeficiente C da sua equação do 2° grau: "))
delta = b**2 - 4*a*c
r1 = (-b + math.sqrt(delta)) / (2*a)
r2 = (-b - math.sqrt(delta)) / (2*a)
print("As raízes são", r1,"e", r2)

#Fim
