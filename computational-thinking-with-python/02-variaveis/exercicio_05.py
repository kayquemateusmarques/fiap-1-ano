# - Exercício 5: Cálculo de uma compra com desconto 
# - Descrição: Faça um programa que solicite o nome de um produto, seu preço unitário, a quantidade 
# comprada e o percentual de desconto oferecido. 

print("===EXERCÍCIO 05===")

# - Entrada de dados
prod = input("Digite o nome do produto: ")
preco = input("Digite o preço unitário: ")
qtd = input("Digite a quantidade: ")
desc = input("Digite o percentual de desconto: ")
desc1 = desc * 0,1
vfinal = (preco * qtd) - desc1

# - Saída de dados
print(f"""
    Produto: = {prod}
    Valor Bruto: = {preco}      
    Desconto: R$ = {desc1}
    Valor final: = {vfinal}
      """)