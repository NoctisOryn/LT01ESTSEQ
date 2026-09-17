#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

#Declarar
d: int = 0
r: float = 0.0

#Início
d = int(input("Digite o valor do depósito: "))
r = d * 1.013
print("Após 1 mês, sua aplicação renderá RS", r)

#Fim
