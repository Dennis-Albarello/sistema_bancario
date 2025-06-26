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
            [7] Clientes Cadastrados
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
    
    '''Função utilizada para que sejam feitos os saques.
    - A variável limite_saldo traz True quando o saldo for maior que o saque;
    - A variável limite_saque traz True quando o saque for menor que o limite disponível para saque;
    - A varável limite_qtde_saque traz True quando a quantidade de saques efetuados for menor que o limite de saques possível'''

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
        print(f"Saque de R${saque:.2f} realizado!")
    
    else:
        print("Valor informado não é válido para essa operação!")

    return saldo , extrato

def gerar_extrato(saldo , / , * , extrato):
    
    '''Função utilizada para que seja visualizado o extrato com as movimentações de Depósitos e Saques. Traz também o total de Saldo Disponível.'''

    print(extrato)
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print("=====================================")

def criar_usuario(dados_usuario):

    '''Função para a criação de usuários dentro do sistema. Inicia-se com a solicitação da identificação do cliente. Com essa informação, através de uma outra função verificamos se este dado de identificação do cliente já consta na base.'''

    cpf = input("Informe o CPF do usuario (somente números):")

    # Checagem do CPF para ver se já existe
    usuario = consulta_cpf(cpf , dados_usuario)

    if usuario is not None:
        print("Usuário já existente para esse CPF informado.")
        return

    nome = str(input("Informe o nome do usuário:"))
    data_nasc = str(input("Informe a data de nascimento do usuário (DD/MM/AAAA):"))
    endereco = str(input("Informe o endereço do usuário:"))

    # Adicionando as informações na lista com os Dados dos Usuários
    dados_usuario.append({
                "nome" : nome ,
                "data_nasc" : data_nasc ,
                "cpf" : cpf ,
                "endereco" : endereco})

    print("Usuário criado com sucesso.")

def consulta_cpf( cpf , dados_usuario):
    '''Função criada de apoio para as funções criar_usuário e criar_conta.'''
    
    busca_cpf = [
        usuario for usuario in dados_usuario if usuario['cpf'] == cpf
        ]
    return busca_cpf[0] if busca_cpf != [] else None
    
def criar_conta(agencia, num_conta, dados_usuario):
    
    '''Através da utilização da função consulta_cpf, cria-se uma conta e a associa a determinado usuário.'''

    # Solicitando o CPF para vincular a um cliente existente
    cpf = input("Informe o CPF do usuario (somente números):")
    # Utilizando-se da função de consulta, capturamos o usuário associado ao CPF
    usuario = consulta_cpf(cpf , dados_usuario)

    if usuario != '':
        print("Conta criada com sucesso.")
        return {
            'agencia' : agencia ,
            'num_conta' : num_conta ,
            "usuario" : usuario}
    
    print("Cliente não encotrado na base de dados!")

def listar_contas(contas):
    
    '''Função criada para listar todas as contas que foram criadas pelo sistema'''

    for conta in contas:
        print("Ag: " + conta['agencia'] +"    " + "C/C: " + str(conta['num_conta']))
        print("Nome: " + conta['usuario']['nome'] +"    " + "CPF: " + conta['usuario']['cpf'])
        print('\n')

def listar_usuarios(contas):
    
    '''Função criada para listar todas os clientes que estão cadastrados no sistema ordenados de acordo com as contas mais recentes criadas.'''

    # Criando variável de contador com o tamanho da lista contas criada
    contador = len(contas) 

    while contador > 0:
        
        print("CPF: " + contas[contador - 1]['usuario']['cpf'] + "\tNome: " + contas[contador - 1]['usuario']['nome'] + "\tC/C: " + str(contas[contador - 1]['num_conta']))
        contador -= 1

def executar_sistema():

    # Definindo as variáveis

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = """\n=====> Extrato de Movimentação <=====:\n\n"""
    numero_saques = 0
    dados_usuario= []
    contas = []
    numero_contas = 1

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
            conta = criar_conta(AGENCIA , numero_contas , dados_usuario )

            if conta != '':
                contas.append(conta)
                numero_contas += 1

    # Listas de Contas dos Usuários

        elif opcao == '6':
            listar_contas(contas)

    # Listas de Clientes Cadastrados

        elif opcao == '7':
            listar_usuarios(contas)

        else:
            break

# Executando o Sistema
executar_sistema()

