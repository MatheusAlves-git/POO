from object import Conta

c1 = Conta(int(input('Número da Conta: ')), str(input('Tipo da conta [CC / CP]: ').upper()),
    str(input('Dono: ')).capitalize(), float(input('Saldo: ')))

c1.abrirConta(c1.saldo)
c1.depositar(float(input('Valor do depósito: ')))
c1.sacar(float(input('Valor do saque: ')))
print(f'Saldo: {c1.saldo}')
c1.pagarMensal()

print(f'\nNúmero da Conta: {c1.numconta}\nTipo: {c1.tipo}\nNome: {c1.dono}\nSaldo: {c1.saldo}')
c1.fecharConta()
