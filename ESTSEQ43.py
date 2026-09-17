# Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria.

#Declarar.
ana: float = 1.10
maria: float = 1.50
anos: int = 0

#Início.
while ana <= maria:
    ana = ana + 0.03
    maria = maria + 0.02
    anos = anos + 1

print(f"Serão necessários {anos} anos.")

#Fim.
