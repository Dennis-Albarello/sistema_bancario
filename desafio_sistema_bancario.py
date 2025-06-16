## Desafio de Projeto Sistema Bancário ##


# Definindo as variáveis

menu = """
######################################
########### MENU DE OPÇÕES ###########
######################################

            [1] Depósito
            [2] Extrato
            [3] Saque
            [0] Sair

######################################
######################################
######################################
→ """

saldo = 0
limite = 500
extrato = """
===> Extrato de Movimentação <===:

"""
numero_saques = 1
LIMITE_SAQUES = 3
deposito = 0
saque = 0


# Desenvolvimento da Inteligência Operacional do Sistema

while True:

    opcao = int(input(menu))

    # Depósitos
    if opcao == 1: 
        deposito = float(input("Informe o valor do Depósito:"))
        
        if deposito > 0:
            saldo += deposito
            extrato += "+ R$ " + str(f'{deposito:.2f}\n')
        else:
            print("Valor informado não é válido para essa operação!")
                        
    # Saques
    elif opcao == 3:
        saque = float(input("Informe o valor do Saque:"))

        limite_saldo = saldo >= saque  # True para realizar o saque
        limite_saque = saque <= limite  # True para realizar o saque
        limite_qtde_saque = numero_saques <= LIMITE_SAQUES  # True para realizar o saque
        
        if limite_saldo == False:
            print("Não há recursos suficientes para o saque desejado.")

        elif limite_saque == False:
            print("Esse saque não é permitido! Valor do saque superior ao limite.")

        elif limite_qtde_saque == False:
            print("Esse saque não foi permitido! Quantidades de saques do dia foram excedidos.")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += "- R$ " + str(f'{saque:.2f}\n')
            

        else:
            print("Valor informado não é válido para essa operação!")

    # Extrato
    elif opcao == 2:
        print(extrato)
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
        print("=================================")
    
    # Saída do sistema
    elif opcao == 0:
        print("\nPrograma finalizado!")
        break
    
    else:
        print("Opção não disponível. Favor inserir com uma opção válida!")




