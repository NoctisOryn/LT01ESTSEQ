#3. Fazer os exercícios abaixo com funções, COM PASSAGEM DE PARÂMETROS:
#a. Fazer um algoritmo que tenha uma função que receba um valor inteiro como parâmetro e retorne seu fatorial. O main deve solicitar ao usuário um valor, chamar a função, receber a saída da função em uma variável e exibir o resultado.
#b. Modificar o exercício 3a e criar uma função que receba 2 parâmetros inteiros e retorne a divisão do primeiro pelo segundo. O main deve solicitar o valor de N e usar as funções para calcular e exibir 1 + 1/1! + 1/2! + ... + 1/N!

#Declarar
a: int = 0

def calc_fat(n):
   i: int = 0
   fat: int = 1
   for i in range(n, 1, -1):
      fat = fat * i
   return fat

def calc_div(n, n2):
   div: float = 0.0
   div = n2 / n
   return div

def main():
   global a
   a = int(input("Digite um número inteiro: "))
   soma: float = 1.0
   for i in range(1, a + 1):
      soma = soma + calc_div(calc_fat(i), 1)
   print(f"O fatorial de {a} é {calc_fat(a)}; enquanto a série é {soma}.")

if (__name__ == '__main__'):
   main();
