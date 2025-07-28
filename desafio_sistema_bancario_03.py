from abc import ABC, abstractmethod, abstractproperty , abstractclassmethod

# Criando as Classes Conta e ContaCorrente (Filha de Conta)

class Conta:
    
    # Função de Iniciação
    def __init__(self , cliente , nro):
        self._saldo = 0
        self._agencia = "0001"
        self._nro = nro
        self._cliente = cliente
        self._historico = Historico()
        
    # Função para acessar o saldo do cliente (Atributo Privado)
    @property
    def saldo(self):
        return self._saldo

    # Função para acessar a agência do cliente (Atributo Privado)
    @property
    def agencia(self):
        return self._agencia

    # Função para acessar o número da conta do cliente (Atributo Privado)
    @property
    def nro(self):
        return self._nro
    
    # Função para acessar o cliente (Atributo Privado)
    @property
    def cliente(self):
        return self._cliente

    # Método de Classe com função para a criação da conta
    @classmethod
    def adicionar_nova_conta(cls, cliente, nro):
        return cls(cliente, nro) # Retornará uma Instância de Conta

    # Função para acessar o histórico do cliente (Atributo Privado)
    @property
    def historico(self):
        return self._historico

    # Função para realizar Depósito na Conta
    def depositar(self, deposito):
        if deposito > 0:
            self._saldo += deposito
            print(f'Depósito de R${deposito:.2f} realizado!')
                
        else:
            print("Valor informado não é válido para essa operação!")
                
    # Função para realizar Saque na Conta
    def sacar(self, saque):
        limite_saldo = saque > self.saldo

        if limite_saldo == True:
            print("Não há recursos suficientes para o saque desejado.")
        
        elif saque > 0:
            self._saldo -= saque
            print(f"Saque de R${saque:.2f} realizado!")

        else:
            print("Valor informado não é válido para essa operação!")
       
class ContaCorrente(Conta):
    def __init__(self, cliente, nro):
        super().__init__(cliente, nro)
        self._limite_saque = 500 # Criação de um Atributo de Instância Privado
        self._limite_qtde_saques = 3 # Criação de um Atributo de Instância Privado
    
    @property
    def limite_saque(self):
        return self._limite_saque
    
    @property
    def limite_qtde_saque(self):
        return self._limite_qtde_saques

    def sacar(self, saque):
        num_saques = 0 
        acima_do_limite = saque > self.limite_saque 
        acima_qtde_saque = num_saques >= self.limite_qtde_saque

        if acima_do_limite == True:
            print("Esse saque não é permitido! Valor do saque superior ao limite.")

        elif acima_qtde_saque == True:
            print("Esse saque não foi permitido! Quantidades de saques do dia foram excedidos.")

        else:
            num_saques += 1 
            return super().sacar(saque) # Utilizará o Método sacar() da Classe Conta

# Criando a Classe Historico

class Historico: 

    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "operacao": transacao.__class__.__name__,
            "valor": transacao.valor,
        })
       
#  Criando a Classe Transacao, Deposito (Filha de Conta) e Saque (Filha de Conta)

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @classmethod
    def registrar(cls, conta):
        deposito_efetuado = conta.depositar(cls.valor)
        if deposito_efetuado == True:
            conta.historico.adicionar_transacao(cls)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @classmethod
    def registrar(cls, conta):
        saque_efetuado = conta.sacar(cls.valor)

        if saque_efetuado == True:
            conta.historico.adicionar_transacao(cls)

#  Criando a Classe Cliente e PessoaFisica (Filha de Conta)

class Cliente:
    def __init__(self , endereco):
        self.endereco = endereco 
        self.contas = [] 
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) # De acordo com a transação, utilizará o Método Registrar 

    def adicionar_conta(self, conta):
        self.contas.append(conta) # Adicionará a Conta na Lista de Contas

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf , nome , data_nascimento):
        super().__init__(endereco) # Chamando o construtor da Classe Pai
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
