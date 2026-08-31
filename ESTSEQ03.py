#Receba a base e a altura de um triângulo. Calcule e mostre a sua área.

#Declarar
base: int = 0
altura: int = 0
área: int = 0

#Início
base = int(input("Digite a base do seu triângulo: "))
altura = int(input("Digete a altura do seu triângulo: "))
área = altura * base / 2
print("A área do seu triângulo é", área)

#Fim
