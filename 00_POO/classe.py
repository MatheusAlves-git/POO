class Caneta:

    def __init__(self, modelo, cor, ponta, carga, tampada=False):
        self.__modelo = modelo
        self.cor = cor
        self.__ponta = ponta
        self.carga = carga
        self.tampada = tampada

    def rabiscar(self, texto):
        if self.tampada:
            print(f'Começou a rabiscar {texto}')
            return

        if not self.tampada:
            print(f'está tampada')
            self.tampada = False
            return

    def parar_rabiscar(self):
        if not self.tampada:
            print(f'Não está rabiscando')
            return

        if self.tampada:
            print(f'Parou de rabiscar')
            self.tampada = False
