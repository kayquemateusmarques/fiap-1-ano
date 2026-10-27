import os
os.system('cls')

v = [45, -89, 32, -12, 33]

# 1 - Retorno do primeiro elemento do vetor
print('Exercício 1: ')
print(v[0])

print()

# 2 - Retorno dos negativos
print('Exercício 2: ')
for ind in range(0,5,1):
    if v[ind] < 0:
        print(f'{v[ind]}')

print()

# 3 - Retorno da soma dos elementos do vetor
soma = 0
print('Exercício 3: ')
for ind in range(0,5,1):
    soma = soma + v[ind]
print(soma)

print()

# 4 - Retorno da media dos elementos do vetor
soma = 0
media = 0
print('Exercício 4: ')
for ind in range(0,5,1):
    soma = soma + v[ind]
    media = soma / 5 
print(media)

print()

# 5 - Retorno dos ímpares
print('Exercício 5: ')
for ind in range(0,5,1):
    if v[ind] % 2 != 0:
        print(f'{v[ind]}')

print()

# 6 - Verificar se a entrada do usuário existe no vetor
num = int(input('Número: '))
if num == v[0] or v[1] or v[2] or v[3] or v[4]:
    print(f'O valor {num} existe no vetor.')
else:
    print(f'O valor {num} não existe no vetor.')