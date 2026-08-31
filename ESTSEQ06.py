#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

#Declarar
x: int = 0
y: int = 0
troca: int = 0

#Início
x = int(input("Digite qualquer número inteiro para ocupar a variável x: "))
troca = x
y = int(input("Digite outro número inteiro para ocupar a variável y: "))
x = y
y = troca
print("O valor na variável x é", x, "enquanto y é", y)
#FIm