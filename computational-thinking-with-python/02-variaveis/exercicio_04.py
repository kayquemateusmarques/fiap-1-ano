# - Exercício 4: Salário mensal
# - Descrição: Faça um programa que solicite o valor recebido por hora trabalhada e a quantidade de horas 
# trabalhadas durante o mês. Calcule e apresente o salário total do funcionário.

print("===EXERCÍCIO 04===")

# - Entrada de dados
hora = float(input("Digite o valor da hora trabalhada: "))
qtd = float(input("Digite a quantidade de horas trabalhadas: "))
salario = hora * qtd

# - Saída do resultado
print(f"O salário do funcionário é R${salario:.2f}")
    