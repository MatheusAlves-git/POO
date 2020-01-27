class Conta:

    def __init__(self, numconta, tipo, dono, saldo, status=False):
        self.numconta = numconta
        self.tipo = tipo
        self.__dono = dono
        self.__saldo = saldo
        self.__status = status


    def construtor(self):
        self.__saldo = 0
        self.__status = False


    def abrirConta(self):
        self.__status = True
        if self.tipo == 'CC':
            self.__saldo = 50   # Valor a mais pra quem abre conta "CC"

        elif self.tipo == 'CP':
            self.__saldo = 150   # Valor a mais pra quem abre conta "CC"


    def fecharConta(self):
        if self.__saldo > 0:
            print('Conta com dinheiro!')
        elif self.__saldo < 0:
            print('Conta em débito!')
        else:
            self.__status = False


    def depositar(self, valor):
        if self.__status is True:
            self.__saldo = self.__saldo + valor
            print(f'Saldo: {self.__saldo}')
        else:
            print('Impossivel depositar!')


    def sacar(self, valor):
        if self.__status is True:
            if self.__saldo > valor:
                self.__saldo = self.__saldo - valor
            else:
                print('Saldo insuficiente!')
        else:
            print('Impossivel sacar!')


    def pagarMensal(self): # Mensalidade da conta
        v = 0
        if self.tipo == 'CC':
            v = 12
        elif self.tipo == 'CP':
            v = 20

        if self.__status is True:
            if self.__saldo > v:
                self.__saldo -= v
            else:
                print('Saldo insuficiente!')
        else:
            print('Impossivel efetuar o pagameento!')
