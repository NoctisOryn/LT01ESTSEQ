#    21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#        a. Se a média for >= 6,0 exibir “APROVADO”;
#        b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
#        c. Se a média for < 3,0 exibir “RETIDO”.

#Declarar.
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
media: float = 0.0

#Início.
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"Média: {media:.1f}")

if media >= 6.0:
    print("APROVADO")
elif media >= 3.0:
    print("EXAME")
else:
    print("RETIDO")

#Fim.