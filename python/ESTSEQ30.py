#Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.

#Declarar.
ano_nasc: int = 0
mes_nasc: int = 0
dia_nasc: int = 0

ano_atual: int = 0
mes_atual: int = 0
dia_atual: int = 0

anos: int = 0
meses: int = 0
dias: int = 0

#Início.
ano_nasc = int(input("Digite o ano de nascimento: "))
mes_nasc = int(input("Digite o mês de nascimento: "))
dia_nasc = int(input("Digite o dia de nascimento: "))

ano_atual = int(input("Digite o ano atual: "))
mes_atual = int(input("Digite o mês atual: "))
dia_atual = int(input("Digite o dia atual: "))

anos = ano_atual - ano_nasc
meses = mes_atual - mes_nasc
dias = dia_atual - dia_nasc

if dias < 0:
    meses = meses - 1

    if mes_atual == 1:
        dias = dias + 31
    elif mes_atual == 2:
        dias = dias + 31
    elif mes_atual == 3:
        if (ano_atual % 4 == 0 and ano_atual % 100 != 0) or ano_atual % 400 == 0:
            dias = dias + 29
        else:
            dias = dias + 28
    elif mes_atual == 4:
        dias = dias + 31
    elif mes_atual == 5:
        dias = dias + 30
    elif mes_atual == 6:
        dias = dias + 31
    elif mes_atual == 7:
        dias = dias + 30
    elif mes_atual == 8:
        dias = dias + 31
    elif mes_atual == 9:
        dias = dias + 31
    elif mes_atual == 10:
        dias = dias + 30
    elif mes_atual == 11:
        dias = dias + 31
    elif mes_atual == 12:
        dias = dias + 30

if meses < 0:
    anos = anos - 1
    meses = meses + 12

print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

#Fim.
