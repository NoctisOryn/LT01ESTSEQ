#Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
#-----------------------
#|Casa: 1 2 3 4	... 64 |
#|---------------------|
#|Qdte:	1 2 4 8	... N  |
#-----------------------

#Declarar.
c: int = 0
g: int = 1
box: int = 0

#Início.
for c in range(1, 65):
   box = box + g
   g = g * 2
print(f"O tabuleiro contém {box} grãos.")
#Fim.
