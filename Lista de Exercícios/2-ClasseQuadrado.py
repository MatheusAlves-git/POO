class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def lado_novo_valor(self, valor):
        self.lado = valor

    def retornar_lado(self):
        print(f'Lado: {self.lado} metros')

    def area(self):
        print(f'Área: {self.lado * self.lado} m²')


while True:
    quad = Quadrado(float(input('Lado do quadrado: ')))
    quad.retornar_lado()
    quad.area()
    quad.lado_novo_valor(float(input('Novo valor para o lado: ')))
    quad.retornar_lado()
    quad.area()
