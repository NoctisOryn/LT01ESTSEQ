#Receba a quantidade horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

#Declarar
qh: int = 0
vh: int = 0
desc: float = 0.0
ndep: int = 0
salário: float = 0.0

#Início
qh = int(input("Digite a quantidade de horas trabalhadas: "))
vh = int(input("Digite o valor por hora: "))
desc = float(input("Digite o percentual de desconto: "))
ndep = int(input("O empregado possui quantos dependentes? (Caso não houver, coloque 0) "))

salário = (qh * vh) - (qh * vh * (desc / 100)) + (100 * ndep)

print(f"O salário líquedo será R${salário}.")

#Fim