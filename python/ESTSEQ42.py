#Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

#Declarar.
n: int = 0
den: int = 0
soma: float = 0.0

#Início.
for n in range(1, 51):
    den = 2 * n - 1
    soma = soma + (n / den)

print(f"O resultado da série é {soma}")

#Fim.
