## Desafio de Projeto Sistema Bancário ##

# %%

## Definindo as funções:

def menu_de_opcoes(): #Ok
    menu = """
    ######################################
    ########### MENU DE OPÇÕES ###########
    ######################################

            [1] Depósito
            [2] Extrato
            [3] Saque
            [4] Nova Conta
            [5] Contas de Usuário
            [6] Novo Usuário
            [0] Sair

    ######################################
    ######################################
    ######################################
    → """
    return input(menu)

def depositar( deposito , saldo , extrato ,/): #OK
            
    if deposito > 0:
        saldo += deposito
        extrato += "\t+ R$ " + str(f'{deposito:.2f}\n')
        print(f'Depósito de R${deposito:.2f} realizado!')

    else:
        print("Valor informado não é válido para essa operação!")
    
    return saldo , extrato

def sacar( *, saque, saldo, extrato, limite, numero_saques, limite_saque ): #OK
    
    limite_saldo = saldo >= saque  # True para realizar o saque
    limite_saque = saque <= limite  # True para realizar o saque
    limite_qtde_saque = numero_saques <= limite_saque  # True para realizar o saque
        
    if limite_saldo == False:
        print("Não há recursos suficientes para o saque desejado.")

    elif limite_saque == False:
        print("Esse saque não é permitido! Valor do saque superior ao limite.")

    elif limite_qtde_saque == False:
        print("Esse saque não foi permitido! Quantidades de saques do dia foram excedidos.")

    elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += "\t- R$ " + str(f'{saque:.2f}\n')
            print(f"Saque de R${saque:.2f} realizado!")
    
    else:
        print("Valor informado não é válido para essa operação!")

    return saldo , extrato

def gerar_extrato(saldo , / , * , extrato): #OK
    print(extrato)
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print("=====================================")

#def criar_usuario(dados_usuario):

        
#def criar_conta(agencia, num_conta, dados_usuario):

#def listar_contas(contas):

def main():

    # Definindo as variáveis

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = """\n=====> Extrato de Movimentação <=====:\n\n"""
    numero_saques = 1
    #deposito = 0
    #saque = 0

    # Desenvolvimento da Inteligência Operacional do Sistema

    while True:

        opcao = menu_de_opcoes()

        # Depósitos

        if opcao == '1':
            
            deposito = float(input("Informe o valor do Depósito:"))
            
            saldo , extrato = depositar( deposito , saldo , extrato )

            saldo
            extrato
        
        # Saques

        elif opcao == '3':

            saque = float(input("Informe o valor do Saque:"))

            saldo, extrato = sacar(
                saque=saque , 
                saldo=saldo , 
                extrato=extrato ,
                limite=limite ,
                numero_saques=numero_saques ,
                limite_saque=LIMITE_SAQUES)
        
        elif opcao == '2':
            gerar_extrato(saldo , extrato=extrato)

        else:
            break
   
                          
# %%

main()


# %%


# RASCUNHO CRIAR USUÁRIO

usuarios = []


# %% 
nome = str(input("Informe o nome do usuario:"))
data_nasc = str(input("Informe a data de nascimento (DD/MM/AAAA):"))
cpf = str(input("Informe o CPF do usuario:"))
endereco = str(input("Informe o endereço do usuario:"))

usuarios.append({
                                "nome" : nome ,
                                "data_nasc" : data_nasc ,
                                "cpf" : cpf ,
                                "endereco" : endereco})


# %%

for usuario in usuarios:
    print(usuario)

# %%

teste = '4' 

for i in usuarios:
    if teste in i['cpf']:
        print("Consta!")
    
# %%
