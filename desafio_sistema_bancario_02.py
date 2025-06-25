## Desafio de Projeto Sistema Bancário ##

## Definindo as funções:

def menu_de_opcoes():
    menu = """
    ######################################
    ########### MENU DE OPÇÕES ###########
    ######################################

            [1] Depósito
            [2] Extrato
            [3] Saque
            [4] Novo Usuário
            [5] Nova Conta
            [6] Contas de Usuários
            [0] Sair

    ######################################
    ######################################
    ######################################
    → """
    return input(menu)

def depositar( deposito , saldo , extrato ,/):
    
    '''Função utilizada para que sejam feitos os depósitos'''
    
    if deposito > 0:
        saldo += deposito
        extrato += "\t+ R$ " + str(f'{deposito:.2f}\n')
        print(f'Depósito de R${deposito:.2f} realizado!')

    else:
        print("Valor informado não é válido para essa operação!")
    
    return saldo , extrato

def sacar( *, saque, saldo, extrato, limite, numero_saques, num_limite_saque ):
    
    limite_saldo = saldo >= saque  # True para realizar o saque
    limite_saque = saque <= limite  # True para realizar o saque
    limite_qtde_saque = numero_saques < num_limite_saque  # True para realizar o saque
        
    if limite_saldo == False:
        print("Não há recursos suficientes para o saque desejado.")

    elif limite_saque == False:
        print("Esse saque não é permitido! Valor do saque superior ao limite.")

    elif limite_qtde_saque == False:
        print("Esse saque não foi permitido! Quantidades de saques do dia foram excedidos.")

    elif saque > 0:
        saldo -= saque
        extrato += "\t- R$ " + str(f'{saque:.2f}\n')
#        numero_saques += 1
        print(f"Saque de R${saque:.2f} realizado!")
    
    else:
        print("Valor informado não é válido para essa operação!")

    return saldo , extrato

def gerar_extrato(saldo , / , * , extrato):
    print(extrato)
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print("=====================================")

def criar_usuario(dados_usuario):
    cpf = input("Informe o CPF do usuario (somente números):")

    # Checagem do CPF para ver se já existe
    usuario = consulta_cpf(cpf , dados_usuario)

    if usuario:
        print("Usuário já existente para esse CPF informado.")
        return

    nome = str(input("Informe o nome do usuario:"))
    data_nasc = str(input("Informe a data de nascimento (DD/MM/AAAA):"))
    endereco = str(input("Informe o endereço do usuario:"))

    dados_usuario.append({
                "nome" : nome ,
                "data_nasc" : data_nasc ,
                "cpf" : cpf ,
                "endereco" : endereco})

    print("Usuário criado com sucesso.")

def consulta_cpf( cpf , dados_usuario):
    busca_cpf = [
        usuario for usuario in dados_usuario if usuario['cpf'] == cpf
        ]
    return busca_cpf[0] if busca_cpf else None
    
def criar_conta(agencia, num_conta, dados_usuario):
    # Solicitando o CPF para vincular a um cliente existente
    cpf = input("Informe o CPF do usuario (somente números):")
    # Utilizando-se da função de consulta, capturamos o usuário associado ao CPF
    usuario = consulta_cpf(cpf , dados_usuario)

    if usuario:
        print("Conta criada com sucesso.")
        return {'agencia' : agencia , 'num_conta' : num_conta , "usuario" : usuario}
    
    print("Cliente não encotrado na base de dados!")

def listar_contas(contas):
    for conta in contas:
        print(conta)

def main():

    # Definindo as variáveis

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = """\n=====> Extrato de Movimentação <=====:\n\n"""
    numero_saques = 0
    dados_usuario= []
    contas = []


    # Desenvolvimento da Inteligência Operacional do Sistema

    while True:

        opcao = menu_de_opcoes()

    # Depósitos

        if opcao == '1':
            # Associando a uma variável a entrada do valor do Depósito
            deposito = float(input("Informe o valor do Depósito:"))
            
            # Retornando o Saldo e o Extrato após o depósito realizado
            saldo , extrato = depositar( deposito , saldo , extrato )

    # Extrato

        elif opcao == '2':
            gerar_extrato(saldo , extrato=extrato)

    # Saques

        elif opcao == '3':
            # Associando a uma variável a entrada do valor do Saque
            saque = float(input("Informe o valor do Saque:"))

            # Retornando o Saldo e o Extrato após o saque realizado
            saldo, extrato = sacar(
                saque=saque , 
                saldo=saldo , 
                extrato=extrato ,
                limite=limite ,
                numero_saques=numero_saques ,
                num_limite_saque=LIMITE_SAQUES)
            
            numero_saques += 1
    # Novo Usuário    
        
        elif opcao == '4':
            criar_usuario(dados_usuario)

    # Criação de Contas
        
        elif opcao == '5':
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA , num_conta , dados_usuario )

            if conta:
                contas.append(conta)

    # Listas de Contas dos Usuários

        elif opcao == '6':
            listar_contas(contas)

        else:
            break
   

main()