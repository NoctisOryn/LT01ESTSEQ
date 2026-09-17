#Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

#Declarar
salário: int = 0
salárioAjus: int = 0

#Início
salário = int(input("Digite o salário atual: "))
salárioAjus = salário * 1.15
print(f"O salário após o reajuste de 15% será de R${salárioAjus}.")

#Fim
