class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def retornar_valor(self):
        print(f'Base: {self.base} \nAltura: {self.altura}')

    def calcular_area(self):
        area = self.base * self.altura
        print(f'Área: {area} m²')
        return area

    def calcular_perimetro(self):
        print(f'Perimetro: {(self.base * 2) + (self.altura * 2)}')


obj = Retangulo(float(input('Base: ')), float(input('Altura: ')))
tam_piso = float(input('Tamanho do piso em metros quadrados: '))
comprimento_rodape = float(input('Comprimento do rodapé: '))

while True:
    print('-'*25)
    obj.retornar_valor()
    obj.calcular_area()
    obj.calcular_perimetro()
    quant_piso = (obj.altura * obj.base) / tam_piso
    print(f'Quantidade de piso: {quant_piso}')
    quant_rodape = (obj.base * 2 + obj.altura * 2) / comprimento_rodape
    print(f'Quantidade de rodapés: {quant_rodape}')
    print('-'*25)

    continuar = str(input('Deseja continuar? [S / N]: ')).upper()
    if continuar == 'N':
        print('Programa finalizado!')
        break

    obj.mudar_valor_lados(float(input('Novo valor de Base: ')), float(input('Novo valor da Altura: ')))

