# 1. Dado um valor numérico pelo usuário, informe o dia da semana correspondente.
# ENTRADA: 2     SAÍDA: Segunda-feita
# ENTRADA: 8     SAÍDA: Valor inválido

# 2. Dado um valor numérico pelo usuário, informe o mês correspondente.
# ENTRADA: 3      SAÍDA: Março
# ENTRADA: -1     SAÍDA: Valor inválido

# 3. Dada uma letra pelo usuário, informar se ela é volgal ou consoante.
# ENTRADA: E      SAÍDA: Vogal
# ENTRADA: m      SAÍDA: consoante
# ENTRADA: @      SAÍDA: Não é letra

# 4. Dados dois valores e um sinal (+, -, * ou /), efetue o calculo correspondente. Lembre-se que 
# em caso de divisão por zero, não há como dividir:
# ENTRADA: 20 + 3      SAÍDA: 23
# ENTRADA: 12 $ 4      SAÍDA: Operador inválido
# ENTRADA: 34 / 0      SAÍDA: Não há divisão por zero

# 5. Dado um valor inteiro com os 3 ultimos digitos da placa de um carro, informar o dia do rodizio
# finais 1 ou 2 - Segunda-feira
# finais 3 ou 4 - Terça-feira
# finais 5 ou 6 - Quarta-feira
# finais 7 ou 8 - Quinta-feira
# finais 9 ou 0 - Sexta-feira

# ENTRADA: 879      SAÍDA: Sexta-feira
# ENTRADA: 321      SAÍDA: Segunda-feira

# Recurso: letra - letra.lower()

import os
os.system("cls")

print(f"""
1 - Exercício um
2 - Exercício dois
3 - Exercício três
4 - Exercício quatro
5 - Exercício cinco
6 - SAIR
""")

opcao = int(input("Digite um número de 1 a 5 e escolha sua opção, ou digite 6 para SAIR: "))

match opcao:
    case 1:
        print(f"Rodando o exercício um...")
        dia = int(input("Digite o número do dia da semana: "))
        match dia:
            case 1 | 2 | 3 | 4 | 5:
                match dia:
                    case 2:
                        print(f"Segunda-feira")
                    case 3:
                        print(f"Terça-feira")
                    case 4:
                        print(f"Quarta-feira")
                    case 5:
                        print(f"Quinta-feira")
                    case 6:
                        print(f"Sexta-feira")
            case _:
                print("Valor inválido!")
                os.kill        

    case 2:
        print(f"Rodando o exercício dois...")
        mes = int(input("Digite o número do mês correspondente: "))
        match mes:
            case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 9 | 10 | 11 | 12:
                match mes:
                    case 1:
                        print(f"Janeiro")
                    case 2:
                        print(f"Fevereiro")
                    case 3:
                        print(f"Março")
                    case 4:
                        print(f"Abril")
                    case 5:
                        print(f"Maio")
                    case 6:
                        print(f"Junho")
                    case 7:
                        print(f"Julho")
                    case 8:
                        print(f"Agosto")
                    case 9:
                        print(f"Setembro")
                    case 10:
                        print(f"Outubro")
                    case 11:
                        print(f"Novembro")
                    case 12:
                        print(f"Dezembro")
            case _:
                print("Valor inválido!")
                os.kill

    case 3:
        print(f"Rodando o exercício três...")
        letra = input("Digite a letra para saber se é vogal ou consoante")
        match letra:
                case 'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U':
                    print(f"Vogal")
                case 'b' | 'B' | 'c' | 'C' | 'd' | 'D' | 'f' | 'F' | 'g' | 'G' | 'h' | 'H' | 'j' | 'J' | 'k' | 'K' | 'l' | 'L' | 'm' | 'M' | 'n' | 'N' | 'p' | 'P' | 'q' | 'Q' | 'r' | 'R' | 's' | 'S' | 't' | 'T' | 'v' | 'V' | 'w' | 'W' | 'y' | 'Y' | 'z' | 'Z':
                    print(f"Consoante")
                case _:
                    print(f"Não é letra!")

    case 4:
        print(f"Rodando o exercício quatro...")
        valor_um = float(input("Digite o primeiro valor:"))
        valor_dois = float(input("Digite o segundo valor:"))
        operacao = input("Digite a operação desejada: ")
        match operacao:
            case '+' | '-' | '*' | '/':    
                match operacao:
                    case '+':
                        print(valor_um + valor_dois)
                    case '-':
                        print(valor_um - valor_dois)
                    case '*':
                        print(valor_um * valor_dois)
                    case '/':
                        if valor_um == 0 or valor_dois == 0:
                            print(f"Não há divisão por zero")
                        else:
                            print(valor_um / valor_dois)
            case _:
                print(f"Operador inválido!")

    case 5:
        print(f"Rodando o exercício cinco...")
        placa = int(input("Digite os 3 últimos dígitos da sua placa: "))
        digito = placa // 10
        valor = placa - (digito * 10)
        match valor:
            case 1 | 2:
                print(f"Segunda-feira")
            case 3 | 4:
                print(f"Terça-feira")
            case 5 | 6:
                print(f"Quarta-feira")
            case 7 | 8:
                print(f"Quinta-feira")
            case 9 | 0:
                print(f"Sexta-feira")

    case 6:
        os.kill