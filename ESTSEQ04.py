#Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.

#Declarar
c: int = 0
f: int = 0

#Início 
c = int(input("Digite a temperatura em graus celsius: "))
f = (9*c + 160) / 5
print(f"Sua temperatura em fahrenheit é {f}°F")

#Fim