#Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX² + BX + C = 0. Verifique e mostre a existência de raízes reais e, caso existam, calcule e mostre.

#Declarar.
a: float = 0.0
b: float = 0.0
c: float = 0.0
delta: float = 0.0
x1: float = 0.0
x2: float = 0.0

#Início.
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"Existe uma raiz real: {x1}")
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)

        print(f"Existem duas raízes reais: {x1} e {x2}")

#Fim.
