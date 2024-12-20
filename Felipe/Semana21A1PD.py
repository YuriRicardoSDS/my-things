class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []
    
    def consultar_saldo(self):
        print("Saldo: R$", self.saldo)
        
    def consultar_transacoes(self):
        print("Transacoes:", self.transacoes)
    
    def depositar(self, valor):
        self.saldo += valor
        print("Você depositou: R$", valor)
        self.registrar_transacao("Depósito", valor)
        
    def registrar_transacao(self, tipo, valor):
        self.transacoes.append({"Tipo": tipo, "Valor": valor})
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
            print("Você sacou : R$", valor)
        else:
            print("Saldo insuficiente.")
    

# cb = ContaBancaria("5542779")
# cb.consultar_saldo()
# cb.depositar(50)
# cb.consultar_saldo()
# cb.consultar_transacoes()
# cb.sacar(45)
# cb.consultar_saldo()

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial=0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial
    def emitir_cheque(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor:
            self.saldo -= valor
            self.registrar_transacao("Emissão de Cheque", valor)
        else:
            print("Limite de cheque especial excedido.")

class ContaPoupanca(ContaBancaria):
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * (taxa_juros / 100)
        self.saldo += juros
        self.registrar_transacao("Juros Mensais", juros)


class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta):
        super().__init__(numero_conta, saldo=0)
        self.investimentos = []
    def registrar_investimentos(self, tipo, produto, valor):
        self.investimentos.append({"Tipo": tipo , "Produto": produto, "Valor": valor})
    
        

# cc = ContaCorrente("88990011",1000)
# cc.depositar(500)
# cc.emitir_cheque(1000)
# cc.consultar_saldo()
# cc.emitir_cheque(400)
# cc.consultar_saldo()
# cc.emitir_cheque(400)

# cp = ContaPoupanca("9293847983", 9000)
# cp.calcular_juros_mensal(0.4)

ci = ContaInvestimento("2234124213")
ci.registrar_investimentos("Tesouro Direto", "Taxa Selic", 2500)
print(ci.investimentos)


