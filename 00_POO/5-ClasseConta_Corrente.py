class ContaCorrente:
    def __init__(self, num_conta, nome_correntista, saldo=0):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = (str(input('Novo Nome: ')))

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor


correntista = ContaCorrente(int(input('Número da conta: ')), str(input('Nome: ')).upper())

print('='*25)
print(f'''Nome: {correntista.nome_correntista}
Número da conta: {correntista.num_conta}
Saldo: {correntista.saldo}''')
print('='*25)

correntista.alterar_nome()
correntista.depositar(float(input('Valor a depositar: ')))
correntista.saque(float(input('Valor a sacar: ')))

print('='*25)
print(f'''Nome: {correntista.nome_correntista}
Número da conta: {correntista.num_conta}
Saldo: {correntista.saldo}''')
print('='*25)
