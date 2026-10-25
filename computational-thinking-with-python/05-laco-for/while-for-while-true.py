# - Laço for: quanto eu souber a quantidade de voltas.
# Exemplo 1 - Repte "Boa noite" 3x
for volta in range(0,3,1):
    print("Boa noite")

# Variável volta começa em 0.
# Depois volta e acrescenta 1.
# Continua no intervalo de 0 a 10? Então, continua executando.
# Só vai até 1 antes

# Exemplo 2 - While improvisado (se eu sei o numero, nao uso while)
# Laço pré-condicional
print("---Execução do while---")
volta = 0
while volta < 10:
    # print("Boa noite") # Para nao pular de linha end = "" dentro do print
    # volta = volta + 1
    print("Boa noite", end = " | ")
    volta = volta + 1

# Exemplo 3 - while True
while True:
    print("Boa noite")
    volta = volta + 1
    if volta >= 10:
        break

# Laço for
variavel = 1
for variavel in range (1,11):
    print(variavel)
# Não tem necessidade de colocar a 3 condição dentro do parentese se ela for 1, pode deixá-la vazia.