# Mostre todas as possibilidades de 2 dados de forma que a soma tenha 7 como resultado.

# Declarar.
d1: int = 0
d2: int = 0

# Início.
for d1 in range(1, 7):
    for d2 in range(1, 7):
        if d1 + d2 == 7:
            print(f"Dado 1: {d1} | Dado 2: {d2}")

# Fim.
