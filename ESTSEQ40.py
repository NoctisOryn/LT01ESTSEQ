# Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

# Declarar.
n1: int = 0
n2: int = 0
i: int = 0
j: int = 0
divisor: int = 0

# Início.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

while n2 == n1:
    n2 = int(input("Digite outro número diferente do primeiro: "))

if n1 > n2:
    temp = n1
    n1 = n2
    n2 = temp

for i in range(n1, n2 + 1):
    divisor = 0

    for j in range(2, i):
        if i % j == 0:
            divisor = divisor + 1

    if divisor == 0 and i >= 2:
        print(i)

# Fim.
