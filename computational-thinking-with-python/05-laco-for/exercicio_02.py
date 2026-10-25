# Imprima os números de 1 a 10
numero = 0
for numero in range(1,11,1):
    print(numero, end = " ")

print()

# Imprima os números em ordem decrescente de 10 a 1
numero = 10
for numero in range(10,0,-1):
    print(numero, end = " ")

print()

# Pulando de 2 em 2
numero = 0
for numero in range(0, 22, 2):
    print(numero, end = " ")

print()

# Exercícios da aula
# 1. Dado o valor inicial e final pelo usuário, exiba os números do intervalo fechado
# ENTRADA: 4     9
# SAÍDA: 4 5 6 7 8 9
v1 = int(input("Primeiro valor: "))
v2 = int(input("Último valor: "))
for v1 in range (v1,v2+1):
    print(v1, end =" ")

print()

# V1.2 Exiba em um formato matemático
# SAÍDA: [4, 5, 6, 7, 8, 9]
num1 = int(input("Digite o primeiro número da sequência: "))
num2 = int(input("Digite o último número da sequência: "))
print("[", end ="")
for num1 in range (num1, num2 + 1):
    print(num1, end ="")
    if num1 < num2:
        print(end = ", ")
print("]", end ="")

print()

# 2. Dado o valor inicial e final pelo usuário, exiba os números do intervalo aberto
# ENTRADA: 4    9
# SAÍDA: 5 6 7 8
v_um = int(input("Digite o primeiro valor: "))
v_um = v_um + 1
v_dois = int(input("Digite o último valor: "))
for v_um in range (v_um, v_dois):
    print(v_um, end = " ")

print()

# V2.2
v_num1 = int(input("Digite o primeiro valor: "))
v_num1 = v_num1 + 1
v_num2 = int(input("Digite o último valor: "))
print("]", end = "")
for v_num1 in range (v_num1, v_num2):
    print(v_num1, end = "")
    if v_num1 < v_num2 -1:
        print(end = ",")
print("[", end = "")