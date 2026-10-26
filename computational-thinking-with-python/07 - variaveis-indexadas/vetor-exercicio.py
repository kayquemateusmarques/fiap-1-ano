import os
os.system('cls')

'''
Exercício:
1. Crie um vetor de inteiro com 5 posições. Peça para o usuário digitar valores em todas as posições, depois exiba o conteúdo de todo o vetor.
'''

# Não deu certo este teste em 2 minutos
# v = []
# qtd = 0
# while qtd < 5: 
#     v = int(input('Digite o valor: '))
#     qtd = qtd + 1
# print(v)

# Execução funcional:
v = [0, 0, 0, 0, 0]

v[0] = input('Digite: ')
v[1] = input('Digite: ')
v[2] = input('Digite: ')
v[3] = input('Digite: ')
v[4] = input('Digite: ')

print(v[0])
print(v[1])
print(v[2])
print(v[3])
print(v[4])

# O problema acima é que é manual, inviável para grandes listas. Dessa forma, eu posso usar laço for:

# Entrada dos dados
# Variável 'ind' começa valendo '0', até '4'
for ind in range(0, 5, 1):
    v[ind] = int(input(f'v[{ind}] = '))

# Exibição dos dados
# Variável 'ind' começa valendo '0', até '4'
for ind in range(0, 5, 1):
    print(f'v[{ind}] = {v[ind]}')

# Se houver necessidade de percorrer todo o vetor, use um laço com as suas dimensões.

'''
Exercício 2: Considerando que o vetor está preenchido, calcule a somatória dos elementos do vetor
'''

# Forma com laço
soma = 0

for ind in range(0,5,1):
    soma = soma + v[ind]

print('soma: ', soma)
print('soma: ', sum(v))
# 'sum' é uma funcao pré-definida do pyhton