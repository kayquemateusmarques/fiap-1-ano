import os
os.system("cls")

num = 1
soma = 0
while num != 0:
    num = float(input("Número: "))
    soma = soma + num
print("Somatória = ", soma)

# - Note que o laço é executado enquanto o número digitado é difernete de 0. Quando eu dou um input 0, ele sai do laço.

opcao = 's'
qtd = 0

while opcao == 's' or opcao == 'S':
    num = float(input("Número: "))
    dobro = num * 2
    print(f"O dobro de {num} é: {dobro}")

    opcao = input("Continuar [s]im ou [n]ão? ")
    qtd = qtd + 1

else: # Quando sai do laço sem interrupção
    print(f"Você calculou {qtd} vezes! Obrigado por usar nosso sistema!")

# Laço pós-condicional não existe em python

qtd = 0

while True:
    num = float(input("Número: "))
    dobro = num * 2
    print(f"O dobro de {num} é: {dobro}")

    opcao = input("Continuar [s]im ou [n]ão? ")
    qtd = qtd + 1

    if opcao == 'n' or opcao == 'N':
        break # interrompe a execução do laço
print(f"Você calculou {qtd} vezes! Obrigado por usar nosso sistema!")
