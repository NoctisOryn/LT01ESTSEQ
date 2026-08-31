#Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
#Declarar
an: int = 0
at: int = 0
id17: int = 0

#Início
an = int(input("Em que ano você nasceu? "))
at = int(input("Em que ano você se encontra nesse momento? "))
id17 = at - an + 17
print(f"Em 17 anos, você terá {id17} anos.")
#Fim