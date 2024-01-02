menu = """
Escolha uma das opções abaixo:

[d] - Depositar
[s] - Sacar 
[e] - Extrato
[q] - Sair

=>"""

saldo = 0
extrato = ""
limite_operacao = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Informe o valor do depósito: "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Operação realizada com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        case "s":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite_operacao
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limire.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
            
        case "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===========================================")
            
        case "q":
            break
        
        case _:
            print("Opção Inválida, por favor selecione novamente a operação desejada.")