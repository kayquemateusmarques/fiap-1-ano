# Estrutura de seleção: match case.
# -> Serve para comparar equivalências, portanto, para comparar se algo é igual a outra coisa.

import os
os.system("cls")

valor = input("Valor: ")
valor = int(valor) # Através deste comando, consigo converter a propria variável em um determinado tipo.

# Exemplo 1
match valor: # comando "match" + o nome da variável
    case 1: # o número "1" neste caso é o uso da equivalência
        print("Digitou um")
    case 2:
        print("Digitou dois")
    case 3:
        print("Digitou três")
    case 4:
        print("Digitou quatro") # caso eu digite algum valor não presente aqui, ele não faz nada.
    case _: # Neste caso, funcionaria como "else" a underline "_"
        print("Digite um valor válido")

# Exemplo 2
match valor: # comando "match" + o nome da variável
    case 1: # o número "1" neste caso é o uso da equivalência
        print("Digitou ímpar")
    case 2:
        print("Digitou par")
    case 3:
        print("Digitou ímpar")
    case 4:
        print("Digitou par") # caso eu digite algum valor não presente aqui, ele não faz nada.
    case _: # Neste caso, funcionaria como "else" a underline "_"
        print("Digite um valor válido")

# Exemplo 2.1
match valor: # comando "match" + o nome da variável
    case 1 | 3: # o número "1" neste caso é o uso da equivalência
        print("Digitou ímpar")
    case 2 | 4:
        print("Digitou par")
    case _: # Neste caso, funcionaria como "else" a underline "_"
        print("Digite um valor válido")