import os
os.system("cls")

# - Entrada de dados
n1 = float(input("Digite a primeira nota: "))
if n1 >= 0 and n1 <= 10:
    n2 = float(input("Digite sua segunda nota "))
    if n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2
        if media > 7 and media < 10:
            mediamais = float(media) + 1.0
            print(f"A média das notas é: {mediamais}")
        else:
            print(f"A média das notas é: {media}")
    else:
        print("Sua segunda nota é inválida! Encerrando o programa.")
else:
    print("Sua primeira nota é inválida! Encerrando o programa.")