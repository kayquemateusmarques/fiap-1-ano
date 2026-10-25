import os
os.system("cls")

while True:
    num = float(input("Número: "))
    if num < 0 or num > 10:
        print("Erro! Número inválido.")
        continue # retorna ao início do programa

    dobro = num * 2
    print(f"O dobro de {num} é: {dobro}")

    opcao = input("Continuar [s]im ou [n]ão? ") 
    while opcao != 'S' and opcao != 's' and opcao != 'n' and opcao != "N":
        opcao = input(("Erro! S ou N? "))
        
    else:
        if opcao == 'n' or opcao == 'N':
            break # interrompe a execução do laço

# Uso de lista -> while opcao not in ['S', 's', 'N', 'n']: