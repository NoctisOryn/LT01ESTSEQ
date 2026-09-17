#Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225.

#Declarar.
n: int = 0
soma: float = 0.0

#Início.
for n in range(1, 16):
    if n % 2 != 0:
        soma = soma + (n / (n ** 2))
    else:
        soma = soma - (n / (n ** 2))

print(f"O resultado da série é {soma}.")

#Fim.
