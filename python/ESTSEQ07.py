#Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

#Declarar
largura: int = 0
comprimento: int = 0
altura: int = 0
volume: int = 0

#Início
largura = int(input("Digite a largura do seu paralelepípedo em cm: "))
altura = int(input("Digite a altura do seu paralelepípedo em cm: "))
comprimento = int(input("Digite a comprimento do seu paralelepípedo em cm: "))
volume = largura * altura * comprimento
print("O volume do seu paralelepípedo é", volume,"cm.")

#Fim
