# - Exercício 1: Antecessor e sucessor
# - Descrição: Faça um programa que solicite um número inteiro e apresente o número informado, seu 
# antecessor e seu sucessor.

print("===Exercício 1===")
# - Entrada de dados
num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
# - Exibição do resultado
print(f"""
    Número informado: {num}
    Antecessor: {ant}
    Sucessor: {suc}
""")
