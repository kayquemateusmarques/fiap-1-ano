import os
os.system('cls')
# Só recebe 1 índice por vez dentro dos colchetes, originalmente.
#     0   1   2   3   4  <== índices    
# O "0" é a numeração do primeiro dado da lista
v = [23, 56, 22, 11, 21]
print(v)    # Exibe toda a estrutura ==> [23, 56, 22, 11, 21]
print(v[1]) # Exibe 56, que corresponde ao índice 1 da lista
print(v[2]) # Exibe 22, que corresponde ao índice 2 da lista

soma = v[0] + v[4]
print(soma)

if v[2] > 30:
    print('É maior do que 30')
else:
    print('Não é maior do que 30')

# Especificamente o Python permite mudar o tipo da variável, de lista para int, por exemplo.
v = [1, 2]
print(v) # Exibe ==> [1, 2] (do tipo lista)
v = 99
print(v) # Exibe ==> 99 (do tipo inteiro)