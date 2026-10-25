print("---Aula-04---")
num = int(input("Digite o seu número: "))
# - Forma Python
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Nulo")
print("---Fim do programa---")

# - Método do professor.
# - De acordo com o professor, eu posso fazer das 2 maneiras.

n = int(input("Digite seu número: "))

# - Apresentação das condições
# - Forma clássica
if n < 0:
    print("Negativo")
else:
    if n > 0:
        print("Positivo")
    else:
        print("Nulo")