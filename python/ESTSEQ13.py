#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

#Declarar
qa: float = 0.0
d: float = 0.0

#Início
qa = float(input("Quantos quilos você possue desse alimento? "))
d = qa * 1000 / 50
print(f"Você poderá consumir este alimento por {d} dias.")

#Fim
